# 6) Random Data Generator
#    - Ask user how many random numbers to generate.
#    - Save them into "random_numbers.csv" as:
#         index,value
#         1, 42
#         2, 87
#         ...
#    - Print total count and average of the generated numbers.

import csv
from typing import List
from random import randint
from decorators import read_positive_int


def generate_nums() -> List[int]:
    limit = read_positive_int("How many numbers to generate: ")
    nums = [randint(1, 100) for _ in range(limit)]

    return nums


def save_in_csv(filename, nums: List[int]) -> None:
    # make sure name is valid
    if not filename.endswith(".csv"):
        filename += ".csv"

    with open(filename, "w") as csvFile:
        writer = csv.writer(csvFile)
        for idx, num in enumerate(nums):
            writer.writerow([idx, num])


def read_from_csv(filename) -> List[int]:
    nums = []
    with open(filename, "r") as csvFile:
        reader = csv.reader(csvFile)

        for idx, num in reader:
            nums.append(num)

    return [int(num) for num in nums]


def print_statistics(nums: List[int]) -> None:
    print(f"Number: {nums}")
    print(f"Total Count: {len(nums)}")
    print(f"Unique Count: {len(set(nums))}")
    print(f"Avg of all nums: {round(sum(nums) / len(nums), 3)}")


def run_random_number_generator() -> None:
    output_file_name = "random_numbers.csv"
    nums = generate_nums()
    save_in_csv(output_file_name, nums)
    data = read_from_csv(output_file_name)
    print_statistics(data)


def main() -> None:
    run_random_number_generator()


if __name__ == "__main__":
    main()
