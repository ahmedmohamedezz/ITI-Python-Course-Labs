# 2) Regex Log Cleaner
#    - Create a file called "access.log" with 10 fake log lines
#      (mix valid emails and invalid strings).
#    - Use regex to extract all valid emails.
#    - Save them into "valid_emails.txt".
#    - Print how many unique emails were found.


# imports
import re
import datetime
from random import randint
from typing import List
from utilities import validate_file_exists


# state vars
log_file = "access.log"
valid_mails_file = "valid_emails.txt"


def create_log_file() -> None:
    # log file structure:
    # (read/write/exe),datetime,email

    actions = ["read", "write", "execute"]
    emails = [
        "alice.smith@example.com",
        "alice.smith@example.com",
        "alice.smith@example.com",
        "user.name@localhost",
        "jane-doe@company.gov",
        "no-at-symbol.com",
        "mary@@example.com",
        "x@short.c",
        "first_last@sub.domain.org",
        "space in@address.com",
    ]

    with open(log_file, "w") as log:
        for i in range(10):
            log.write(
                f"{actions[randint(0, 2)]},{datetime.datetime.now()},{emails[i]}\n"
            )


def extract_valid_emails() -> None:
    # r: for raw string, to avoid syntax warning (invalid escape seq)
    mail_regex = r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.(com|org|gov)$"
    lines = []

    if validate_file_exists(log_file):
        with open(log_file, "r") as log:
            lines = log.readlines()
    else:
        print(f"File {log_file} not found")

    # extract emails from each line after 2nd comma 'action,time,email'
    emails = [line.split(",")[2] for line in lines]

    # filter valid emails
    emails = list(filter(lambda cur_mail: re.match(mail_regex, cur_mail), emails))

    with open(valid_mails_file, "w") as valid_file:
        for email in emails:
            valid_file.write(email)


def read_valid_emails() -> List[int]:
    valid_emails = []

    if validate_file_exists(valid_mails_file):
        with open(valid_mails_file, "r") as valid:
            valid_emails.extend(valid.readlines())
    else:
        print(f"File {valid_mails_file} not found")

    return valid_emails


def count_unique_emails(mails: List[int]) -> int:
    print("valid emails")
    print(mails)
    print("unique valid mails")
    unique = set(mails)
    print(unique)

    return len(unique)


def run_log_cleaner() -> None:
    print("---- Regex Log Cleaner Task(2) ----")
    create_log_file()
    extract_valid_emails()
    mails = read_valid_emails()
    print(count_unique_emails(mails))


def main() -> None:
    run_log_cleaner()


if __name__ == "__main__":
    main()
