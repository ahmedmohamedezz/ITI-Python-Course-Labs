from typing import List
from utilities import is_number


def ensure_non_negative_numbers(func):
    prompt = "Enter non-negative comma-separated numbers ex. (0, 1.2, 4): "

    def wrapper():
        while True:
            # read list of comma-seprated strings
            nums = func(prompt)

            # validate it contain +ve numbers
            if any(not (is_number(num) and float(num) >= 0) for num in nums):
                print("Invalid input")
                continue

            return [float(num) for num in nums]

    return wrapper


def ensure_numbers(func):
    prompt = "Enter comma-separated numbers ex. (-15, 0, 1.2, 4): "

    def wrapper():
        while True:
            # read list of comma-seprated strings
            nums = func(prompt)

            # validate it contain +ve numbers
            if any(not is_number(num) for num in nums):
                continue

            return [float(num) for num in nums]

    return wrapper


def read_comma_separated_strings(msg="Enter a comma-separated string") -> List[str]:
    lst = []
    while True:
        line = input(msg + " ")
        try:
            lst = line.split(",")
        except ValueError:
            print("Invalid input, elements must be comma separated")
            continue

        return lst


# manually apply the decorator, if we want to make sure that the items are numbers
def read_comma_separated_non_negative_nums() -> List[float]:
    return ensure_non_negative_numbers(read_comma_separated_strings)()


def read_comma_separated_nums() -> List[float]:
    return ensure_numbers(read_comma_separated_strings)()


# ------------------------------------------------------------------------
def read_int(msg="Enter an integer. ex (1, -10, 0)") -> int:
    while True:
        try:
            num = int(input(msg + " "))
        except ValueError:
            print("Invalid integer. ex (1, -10, 0)")
            continue
        else:
            return num


def ensure_positive(func):
    def wrapper(msg="Enter a positive integer") -> float:
        while True:
            number = func(msg)
            if number <= 0:
                print("Number must be >= 0")
                continue

            return number

    return wrapper


def read_positive_int(msg):
    return int(ensure_positive(read_int)(msg))
