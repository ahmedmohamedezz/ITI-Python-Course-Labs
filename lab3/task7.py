# 7) Decorators Task
#    - Create a decorator called "log_time" that:
#         - Records the execution time of any function.
#         - Saves the function name and runtime into "execution_log.txt".
#    - Apply this decorator to at least two tasks (e.g., Math Automation & Regex Log Cleaner).
#    - Verify that the log file contains entries after running.

import time


def timer(func):
    output_filename = "execution_log.txt"

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        consumed_time = round(end - start, 7)
        print(
            f"\033[32mTime taken by {func.__name__} function is: {consumed_time} seconds\033[0m"
        )

        with open(output_filename, "a") as output_file:
            output_file.write(f"{func.__name__}: {consumed_time} seconds")

    return wrapper


def log_time(func):
    timer(func)()


def main() -> None:
    def test_function():
        time.sleep(2)

    log_time(test_function)


if __name__ == "__main__":
    main()
