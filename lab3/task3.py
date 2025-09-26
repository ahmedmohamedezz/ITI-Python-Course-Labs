# 3) Datetime Reminder Script
#    - Ask user for a date (YYYY-MM-DD).
#    - Calculate how many days remain until that date.
#    - If it is in the past, print "This date has already passed."
#    - Otherwise, save the reminder into "reminders.txt" in format:
#         "{date} -> {days_left} days left"
#    - Append multiple reminders without overwriting.

import datetime
from utilities import is_number, in_range, validate_file_exists


def read_date() -> str:
    while True:
        reminder_date = input("Enter a date (YYYY-MM-DD): ")
        try:
            year, month, day = reminder_date.split("-")
        except ValueError:
            print("Invalid input")
            continue

        valid = (
            is_number(year)
            and is_number(month)
            and is_number(day)
            and in_range(float(month), 1, 12)
            and in_range(float(day), 1, 30)
        )

        if not valid:
            continue

        return reminder_date


def process_date(date: str, remindes_filename) -> None:
    try:
        # conver to date and compare
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.date.today()

        # calculate days between
        days = (date_obj - today).days

        if days > 0:
            with open(remindes_filename, "a") as rem_file:
                rem_file.write(f"{date_obj.strftime('%Y-%m-%d')} -> {days} days left\n")
        else:
            print("This date has already passed.")

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


def run_datetime_reminder() -> None:
    print("---- Datetime Reminder Task(3) ----")
    remindes_filename = "reminders.txt"

    while True:
        choice = input("Enter -1 to exit, or 1 to add another reminder: ")
        if choice == "-1":
            break
        elif choice != "1":
            print("Invalid choice")
            continue

        # 2 core functions
        date = read_date()
        process_date(date, remindes_filename)

    print("Thank you for using our calender reminder")
    print("reminders: ")

    if validate_file_exists(remindes_filename):
        with open(remindes_filename, "r") as rem_file:
            for line in rem_file.readlines():
                # remove end = '\n', elements already stored with \n
                print(line, end="")
    else:
        print(f"File {remindes_filename} not found")


def main() -> None:
    run_datetime_reminder()


if __name__ == "__main__":
    main()
