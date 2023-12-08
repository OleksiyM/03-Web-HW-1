import logging
import sys
from pathlib import Path
from time import time

from sort import sort_folder, unpack_archives, delete_empty_folders, count_files_in_folders


def main():
    # log_level = logging.INFO
    log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format="[%(asctime)s] %(levelname)s %(threadName)s %(message)s")

    if len(sys.argv) < 2:
        print("Mandatory parameter was not specified")
        print("Usage main.py <Folder>")
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
