"""
------------------------------------------------
Rules:
    1. Every user input must be validated.
       - If invalid, print error and ask again until valid.
    2. Each task must be implemented in a separate .py file.
       - Each file must contain a function that executes the task.
    3. A main.py file must import all task modules.
    4. When main.py runs:
         - Display a menu showing all tasks with their number & name.
         - Let the user select which task to execute by entering the task number.
         - Run only the selected task.
    5. Use if __name__ == "__main__": script only run in main.py`.
    6. Use functions and avoid code duplication.
    7. Add comments explaining each step.
    8. Automate as much as possible (e.g., file creation, processing).
    9. No hardcoding results.
    10. Decorators (Task 7) must be applied to at least two tasks.
------------------------------------------------
"""

from utilities import in_range
from decorators import read_positive_int

from task1 import generate_math_report
from task2 import run_log_cleaner
from task3 import run_datetime_reminder
from task4 import run_product_data_transformer
from task5 import run_os_file_manager
from task6 import run_random_number_generator
from task7 import log_time


def main() -> None:
    while True:
        print()
        print("Choose a number")
        print("1. To run math report script")
        print("2. To run log cleaner script")
        print("3. To run datetimt reminder script")
        print("4. To run product data transformer script")
        print("5. To run os file manager script")
        print("6. To run random number generator script")
        print("7. Exit")

        choice = 0
        st, en = 1, 7
        while True:
            choice = read_positive_int(f"Enter choice ({st}-{en}): ")
            if not in_range(choice, st, en):
                print(f"number not in range [{st}, {en}]")
                continue
            break

        if choice == 9:
            break

        match choice:
            case 1:
                log_time(generate_math_report)
            case 2:
                log_time(run_log_cleaner)
            case 3:
                log_time(run_datetime_reminder)
            case 4:
                log_time(run_product_data_transformer)
            case 5:
                log_time(run_os_file_manager)
            case 6:
                log_time(run_random_number_generator)
            case 7:
                return


if __name__ == "__main__":
    main()
