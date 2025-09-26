import os

# file operations
def validate_file_exists(filename) -> bool:
    if os.path.exists(filename):
        return True

    return False


def print_file_content(filename) -> None:
    with open(filename, "r") as f:
        print(f.read())


# ------------------------------------------------------------------------------------
# check if number (float/int)
def is_number(num):
    try:
        num = float(num)
        return True
    except ValueError:
        return False


# check if number falls in this range [st, en]
def in_range(num: float, st: float, en: float) -> bool:
    return st <= num <= en
