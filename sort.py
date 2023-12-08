import shutil
from pathlib import Path
import sys
import os
from threading import Thread
from time import time
import logging

transliteration_dict = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "yu",
    "я": "ya",

    # Ukrainian characters
    "є": "ye",
    "і": "i",
    "ї": "yi",
    "ґ": "g",

    # Uppercase Cyrillic letters
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "Yo",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "Y",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "Kh",
    "Ц": "Ts",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Ъ": "",
    "Ы": "Y",
    "Ь": "",
    "Э": "E",
    "Ю": "Yu",
    "Я": "Ya",

    # Uppercase Ukrainian characters
    "Є": "YE",
    "І": "I",
    "Ї": "YI",
    "Ґ": "G"

}
CATEGORIES = {"images": [".jpeg", ".png", ".jpg", ".svg", ".gif"],
              "video": [".avi", ".mp4", ".mov", ".mkv", ".wmv"],
              "documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".odt", ".ods"],
              "audio": [".mp3", ".ogg", ".wav", ".amr"],
              "archives": [".zip", ".gz", ".tar"]}

log = []
known_extensions = set()
unknown_extensions = set()


def normalize(filename: str) -> str:
    # Split into filename and extension
    file_ext = ""
    extension_start_index = filename.rfind(".")
    if extension_start_index != -1:
        file_ext = filename[extension_start_index:]
        filename = filename[:extension_start_index]

    normalized_filename = ""

    # Transliterate Cyrillic characters
    for character in filename:
        if character in transliteration_dict:
            normalized_filename += transliteration_dict[character]
        else:
            if character.isalnum():
                # Keep alphanumeric characters
                normalized_filename += character
            else:
                # Pass through non-alphanumeric characters unchanged
                normalized_filename += "_"
    # Return the normalized filename with extension
    return normalized_filename + file_ext


def get_category_name(file: Path) -> str:
    ext = file.suffix.lower()
    for category, exts in CATEGORIES.items():
        if ext in exts:
            return category
    return "other"


def move_file(file: Path, category: str, root_dir: Path) -> None:
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir(exist_ok=True)
        logging.debug(f"Created Folder {target_dir}")

    new_path = target_dir.joinpath(normalize(file.name))
    if file.stem != new_path.stem:
        logging.debug(f"Normilized {file.name} -> {new_path.name}")

    if not new_path.exists():
        file.replace(new_path)
        logging.debug(f"File moved {file} -> {new_path}")
    else:
        file.replace(new_path)
    return


def sort_folder(path: Path) -> None:
    logging.info(f"Started sorting folder {path}")
    threads = []
    for element in path.glob("**/*"):

        if element.is_file():
            category = get_category_name(element)
            if category != "other":
                known_extensions.add(element.suffix)
            else:
                unknown_extensions.add(element.suffix)

            thread = Thread(target=move_file, args=(element, category, path))
            thread.start()
            threads.append(thread)
            # move_file(element, category, path)
    [thread.join() for thread in threads]
    logging.debug(f"All threads finished")
    return


def unpack_archive(file: Path, category: str, root_dir: Path) -> None:
    path_to_unpack = root_dir.joinpath(category).joinpath(normalize(file.stem))
    new_path = root_dir.joinpath(category).joinpath(normalize(file.name))
    try:
        shutil.unpack_archive(file, path_to_unpack)
        file.replace(new_path)
        # os.remove(file)
        logging.debug(f"Archive unpacked {file} -> {path_to_unpack}")
    except:
        logging.error(f"Error unpacking Archive {file}")
    return


def is_archive(file: Path) -> bool:
    ext = file.suffix.lower()
    if ext in CATEGORIES["archives"]:
        return True
    return False


def unpack_archives(root_dir: Path) -> None:
    logging.info(f"Starting unpacking archives")
    category = "archives"
    path = root_dir.joinpath(category)
    threads = []
    for element in path.glob("**/*"):
        if element.is_file() and is_archive(element):
            thread = Thread(target=unpack_archive, args=(element, category, root_dir))
            thread.start()
            threads.append(thread)
    [thread.join() for thread in threads]
    logging.debug(f"All threads finished")
    return


def delete_empty_folders(root_dir) -> None:
    logging.info(f"Deleting empty folders")
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            if not os.listdir(full_path):
                os.rmdir(full_path)
                logging.debug(f"Empty Folder was removed {full_path}")

    return


def count_files_in_folders(root_dir: Path) -> None:
    all_categories = []
    for el in CATEGORIES.items():
        all_categories.append(el[0])
    all_categories.append("other")
    logging.info(f"Counting files in folders {root_dir}")
    logging.info(f"------------------------- Sorting results -------------------------")
    logging.info("Known extensions: " + ", ".join(known_extensions))
    logging.info("Unknown extensions: " + ", ".join(unknown_extensions))

    for el in all_categories:
        category = el

        path_dir = root_dir.joinpath(category)
        files_count = sum(1 for element in path_dir.glob(
            '**/*') if element.is_file())
        logging.info(f"Files in the {category}: {files_count}")
    return


def main():
    # log_level = logging.INFO
    log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format="[%(asctime)s] %(levelname)s %(threadName)s %(message)s")

    if len(sys.argv) < 2:
        print("Mandatory parameter was not specified")
        print("Usage sort.py <Folder>")
        print("Error Code: 1")
        return 1

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"Specified Folder {path} does not exist\nError Code: 2")
        return 2

    if not path.is_dir():
        print(
            f"Parameter: {path} is not a Folder (probably file)\nError Code: 3")
        return 3

    start = time()
    logging.debug(f'Start time: {start}')

    sort_folder(path)

    unpack_archives(path)

    delete_empty_folders(path)

    count_files_in_folders(path)

    end = time()

    logging.debug(f'End time: {end}')
    logging.info(f'Total time: {end - start}')
    logging.info(f'Finished sorting folder {path}')

    return 0


if __name__ == '__main__':
    main()
