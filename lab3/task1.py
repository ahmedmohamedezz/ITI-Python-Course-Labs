# 1) Math Automation
#    - Create a file called "math_report.txt".
#    - Ask the user for multiple numbers (comma-separated).
#    - For each number, calculate:
#         - floor, ceil, square root, area of a circle
#    - Write the results into "math_report.txt".
#    - Confirm file was created and print its content.

import math
from utilities import validate_file_exists, print_file_content
from decorators import read_comma_separated_non_negative_nums


def main() -> None:
    file_name = "math_report.txt"
    generate_math_report(file_name)


def generate_math_report(filename="math_report.txt") -> None:
    # NOTE: -ve numbers will make sqrt throw an exception. so we limit all numbers to be non-negative

    print("---- Math Report Task(1) ----")
    # conditionaly apply the decorator (read comma-separated string, then make sure each is a number)
    nums = read_comma_separated_non_negative_nums()

    with open(filename, "w") as report:
        for idx, val in enumerate(nums):
            if not idx:
                # write header line
                report.write(
                    # <x display left aligned with width = x characters
                    # ^x cener
                    # >x right-aligned
                    f"{'Idx':<3} {'Floor':<5} {'Ceil':<5} {'Square':<5} {'Cicle Area':^10}\n"
                )

            report.write(
                f"{idx:<1})  {math.floor(val):<6} {math.ceil(val):<5} {round(math.sqrt(val), 3):<5} {round(math.pi * math.pow(val, 2), 3):^10}\n"
            )

    # validate file exitst and print it's content
    if validate_file_exists(filename):
        print("Report: ")
        print_file_content(filename)
    else:
        print(f"File {filename} not found")


if __name__ == "__main__":
    main()
