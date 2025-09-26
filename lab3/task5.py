# 5) OS File Manager
#    - Ask user for a directory path.
#    - Automatically:
#         - Create a folder "backup" inside it if not exists.
#         - Copy all .txt files into "backup".
#         - Print summary: how many files copied.
#    - If directory invalid, retry until correct.
import os
import shutil


def run_os_file_manager():
    while True:
        dir_path = input("Enter directory path: ")
        dir_path.strip()  # avoid extra spaces

        # Check if directory exists
        if not os.path.isdir(dir_path):
            print("Directory doesn't exist\n")
            continue

        # create backup
        backup_path = os.path.join(dir_path, "backup")
        os.makedirs(backup_path, exist_ok=True)

        copied_count = 0

        # copy .txt files only
        for file_name in os.listdir(dir_path):
            # NOTE: suppose files have extension.
            # if not (unix system), the task could be done using 'magic' external package using mime-types
            if file_name.endswith(".txt"):
                src = os.path.join(dir_path, file_name)
                dst = os.path.join(backup_path, file_name)
                shutil.copy(src, dst)
                copied_count += 1

        print(f"{copied_count} text files copied to {backup_path}")
        break


def main() -> None:
    run_os_file_manager()


if __name__ == "__main__":
    main()
