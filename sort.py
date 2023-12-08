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

        # print(f"normilize debug: filename {filename}, ext {file_ext}")

    normalized_filename = ""

    # Transliterate Cyrillic characters
    for character in filename:
        if character in transliteration_dict:
            normalized_filename += transliteration_dict[character]
            # print(character, "->", transliteration_dict[character])
        else:
            if character.isalnum():
                # Keep alphanumeric characters
                normalized_filename += character
                # print(character, "=")
            else:
                # Pass through non-alphanumeric characters unchanged
                normalized_filename += "_"
                # print(character, "->", "_")
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
        target_dir.mkdir()
        logging.debug(f"Created Folder {target_dir}")
        # log.append(f"DIR: {target_dir} was created\n")
    # TODO check exist - count existing files, add increment to the file name
    new_path = target_dir.joinpath(normalize(file.name))
    if file.stem != new_path.stem:
        logging.debug(f"Normilized {file.name} -> {new_path.name}")
        # log.append(f"NORMALIZE: File renamed {file.name} -> {new_path.name}\n")

    if not new_path.exists():
        file.replace(new_path)
        logging.debug(f"File moved {file} -> {new_path}")
        # log.append(f"SORT: File moved {file} -> {new_path}\n")
    else:
        file.replace(new_path)
        # logging.debug(f"Duplicate File moved {file} -> {new_path}")
        # log.append(f"SORT: Duplicate File moved {file} -> {new_path}\n")

    return


def sort_folder(path: Path) -> None:
    logging.info(f"Started sorting folder {path}")
    # log.append(f"LOG: started sorting folder {path}\n")
    for element in path.glob("**/*"):

        if element.is_file():
            # print(element, "\n")
            category = get_category_name(element)
            if category != "other":
                known_extensions.add(element.suffix)
            else:
                unknown_extensions.add(element.suffix)
            # if category == "archives":
            #    unpack_archive(element, category, path)
            # else:
            # print(element, category, path)
            move_file(element, category, path)
    return


def unpack_archive(file: Path, category: str, root_dir: Path) -> None:
    path_to_unpack = root_dir.joinpath(category).joinpath(normalize(file.stem))
    new_path = root_dir.joinpath(category).joinpath(normalize(file.name))
    try:
        shutil.unpack_archive(file, path_to_unpack)
        file.replace(new_path)
        # os.remove(file)
        logging.debug(f"Archive unpacked {file} -> {path_to_unpack}")
        # log.append(f"SORT: Archive unpacked {file} -> {path_to_unpack}\n")
    except:
        logging.error(f"Error unpacking Archive {file}")
        # log.append(f"SORT: Error unpacking Archive {file}\n")
    return


# function is check is file is archive by checking is present extensions in the CATEGORIES dict in the "archives"
def is_archive(file: Path) -> bool:
    ext = file.suffix.lower()
    if ext in CATEGORIES["archives"]:
        return True
    return False


def unpack_archives(root_dir: Path) -> None:
    logging.info(f"Unpacking archives")
    category = "archives"
    path = root_dir.joinpath(category)
    for element in path.glob("**/*"):
        if element.is_file() and is_archive(element):
            path_to_unpack = path.joinpath(normalize(element.stem))
            try:
                shutil.unpack_archive(element, path_to_unpack)
                logging.debug(f"Archive unpacked {element} -> {path_to_unpack}")
                # log.append(f"SORT: Archive unpacked {element} -> {path_to_unpack}\n")
            except:
                logging.error(f"Error unpacking Archive {element}")
                # log.append(f"SORT: Error unpacking Archive {element}\n")
    return


def delete_empty_folders(root_dir) -> None:
    logging.info(f"Deleting empty folders")
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            if not os.listdir(full_path):
                os.rmdir(full_path)
                logging.debug(f"Empty Folder was removed {full_path}")
                # log.append(f"DIR: Empty Directory {full_path} was removed\n")
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
    # log.append("------------------------- Sorting results -------------------------")
    # log.append("\nKnown extensions: " + ", ".join(known_extensions))
    # log.append("\nUnknown extensions: " + ", ".join(unknown_extensions))

    for el in all_categories:
        category = el

        path_dir = root_dir.joinpath(category)
        files_count = sum(1 for element in path_dir.glob(
            '**/*') if element.is_file())
        logging.info(f"Files in the {category}: {files_count}")
        # log.append(f"\nFiles in the {category}: {files_count}")
    return


def write_log_file(path: Path) -> bool:
    log_file = path.joinpath("log.txt")
    print(f"Log file saved in {log_file}")
    # Open log file and write logs
    with open(log_file, "w") as fh:
        for l in log:
            try:
                fh.write(l)
            except:
                print("ERROR writing to the log file:")
                print(l)
                return False
    return True


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

    # write_log_file(path)

    end = time()

    logging.debug(f'End time: {end}')
    logging.info(f'Total time: {end - start}')
    logging.info(f'Finished sorting folder {path}')

    return 0


if __name__ == '__main__':
    main()
