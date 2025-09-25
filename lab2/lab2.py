from random import randint

"""
Python Practice Tasks
=====================

Rules:
    - Everything must be written inside functions.
    - The file should run as a script.
    - When the script starts, the user must see a menu of numbered scenarios  (1: List order, 2: Pepole with favorite color , .....).
    - The user chooses a number, and the program runs the corresponding function.
    - Each task should only run when chosen from the menu.
    - At ANY stage: if the user enters invalid input, the program must:
          * Show an error message
          * Display what valid input looks like
          * Let the user try again (do not crash or exit)
"""


# helper functions
def read_int(msg="Enter an integer. ex (1, -10, 0)") -> int:
    while True:
        try:
            num = int(input(msg + " "))
        except ValueError:
            print("Invalid integer. ex (1, -10, 0)")
            continue
        else:
            return num


def read_float(msg="Enter an number. ex (1, -10, 0, 3.14)") -> float:
    while True:
        try:
            num = float(input(msg + " "))
        except ValueError:
            print("Invalid number. ex (1, -10, 0, 3.14)")
            continue
        else:
            return num


def is_float(s: str) -> bool:
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


def read_alpha(msg) -> str:
    alpha = ""
    while True:
        alpha = input(msg + " ").strip()
        while not alpha.isalpha():
            print("Invalid input. character only allowed")
            alpha = input(msg + " ").startswith()
        return alpha


def in_range(num: int, st: int, en: int) -> bool:
    return st <= num <= en


# 1 - Ask the user to enter 5 numbers.
# Store them, then display them in ascending order and descending order.
def task1() -> None:
    lst = []
    print("Enter 5 numbers: ")
    for i in range(5):
        print(f"num {i + 1}: ")
        num = read_int()
        lst.append(num)

    lst.sort()
    print(lst)
    lst.sort(reverse=True)
    print(lst)


# 2 - Write a function that takes two numbers: (length, start).
#     Generate a sequence of numbers with the given length,
#     starting from the given start number and increasing by one each time.
#     Print the result.
def task2() -> None:
    def run(ln: int, st: int):
        for e in range(st, st + ln):
            print(e, end=" ")

        print()

    ln = read_int("Enter the sequence lengh:")
    st = read_int("Enter the starting number")
    run(ln, st)


# 3 - Keep asking the user for numbers until they type "done".
#     When finished, print:
#         * The total of all numbers entered
#         * The count of valid entries
#         * The average
#     If the user enters something invalid, show an error and continue.
def task3() -> None:
    inp = ""
    sm = cnt = 0
    invalid = 0
    while True:
        inp = input("Enter 'done', or a number. ex (4, 2.2, -4, 0):  ")
        if inp == "done":
            break

        if not is_float(inp):
            invalid += 1
            print("Invalid input, enter 'done', or a number. ex (4, 2.2, -4, 0):  ")
            continue

        inp = float(inp)
        sm += inp
        cnt += 1

    print(f"Total: {sm}")
    print(f"Invaild entries count: {invalid}")
    print(f"Avg: {round(sm / cnt, 3)}")


# 4 - Ask the user to enter a list of numbers.
#     Remove any duplicates, sort the result, and display it.
def task4() -> None:
    num = 0
    lst = []
    while True:
        num = read_int("Enter an int (0, 20, -4), or -999 to stop")
        if num == -999:
            break

        lst.append(num)

    print(sorted(list(set(lst))))


# 6 - Ask the user to enter a sentence.
# Count how many times each word appears in the sentence
# and display the result.
def task6() -> None:
    sen = ""
    while True:
        sen = input("Enter a sentence: ").strip()
        while len(sen) == 0:
            print("Sentence can't be empty")
            sen = input("Enter a sentence: ").strip()
        break

    words = sen.split()
    freq = dict()
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    for k, cnt in freq.items():
        print(f"{k} appeared {cnt} times")


# 7 - Create a small gradebook system:
#     - The user enters 5 students names and their scores.
#     - At the end, show:
#         * The highest score
#         * The lowest score
#         * The average score.
def task7() -> None:
    # not a dict, to allow repeated student names
    students = []

    for i in range(5):
        print(f"{i + 1}th student information: ")
        name = read_alpha(
            "Enter the student name (characters only allowed a-z and A-Z)"
        )
        score = read_float()
        students.append((name, score))

    sm = sum(sc for (_, sc) in students)
    mn = min(sc for (_, sc) in students)

    print(f"Max score: {sm}")
    print(f"Min score: {mn}")
    print(f"Avg score: {(sm / 5):0.3f}")


# 8 - Write a program that simulates a shopping cart:
#     - The user can add items with a name and a price.
#     - The user can remove items by name.
#     - The user can view all items with their prices.
#     - At the end, display the total cost.
def task8() -> None:
    cart = {}

    while True:
        print()
        print("Choose a number")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout")

        choice = 0
        while True:
            choice = read_int("Enter choice (1-4): ")
            if not in_range(choice, 1, 4):
                print("number not in range [1, 4]")
                continue

            break

        if choice == 1:
            name = read_alpha("Enter item name: ")

            if name in cart:
                print("Item already exists. how many more of it you want: ")
                quantity = read_int("Enter the quantity to be added on existing: ")
                cart[name][1] += quantity
            else:
                price = 0  # must be (> 0)
                while True:
                    price = read_float("Enter item price ex (22.35): ")
                    if price <= 0:
                        print("Price can't be <= 0")
                        continue

                    break

                cart[name] = [price, 1]

            print("Added Successfully")

        elif choice == 2:
            name = read_alpha("Enter item name: ")
            if name in cart:
                del cart[name]
                print(f"{name} removed from cart.")
            else:
                print("Item is not in the cart")

        elif choice == 3:
            if not cart:
                print("No items in cart (empty)")
            else:
                tot = 0
                print()
                for item in cart:
                    pr, qn = cart[item]

                    print(f"{item=}, ${pr=:.2f}. quantity: {qn}")
                    tot += pr * qn
                print(f"Total: ${tot:.2f}")

        elif choice == 4:
            total = sum(pr * qn for [pr, qn] in cart.values())
            print("Checkout")
            print(f"Total: {total:0.2f}")
            break


# 9 - Create a number guessing game:
#     - The program randomly selects a number between 1 and 20.
#     - The user keeps guessing until they get it right.
#     - After each guess, show if the guess was too high or too low.
#     - When correct, display the number of attempts.
def task9() -> None:
    attempts = 0
    target = randint(1, 20)

    while True:
        num = read_int("Enter an integer: ")
        if num == target:
            print("Correct!")
            print(f"No. of attempts: {attempts}")
            break
        else:
            attempts += 1
            if num < target:
                print("Too low")
            elif num > target:
                print("Too high")


if __name__ == "__main__":
    while True:
        print()
        print("Choose a number")
        print("1. enter 5 numbers. see them in ascending order and descending order")
        print("2. Generate a sequence of numbers with the given length")
        print("3. Numbers statistics (max, min, avg)")
        print("4. Remove duplicates from numbers and sort them")
        print("5. Count occurences in sentence")
        print("6. Gradebook system. student names and scores")
        print("7. Shopping cart")
        print("8. Geussing game")
        print("9. Exit")

        choice = 0
        while True:
            choice = read_int("Enter choice (1-9): ")
            if not in_range(choice, 1, 9):
                print("number not in range [1, 9]")
                continue
            break

        if choice == 9:
            break

        match choice:
            case 1:
                task1()
            case 2:
                task2()
            case 3:
                task3()
            case 4:
                task4()
            case 5:
                task6()
            case 6:
                task7()
            case 7:
                task8()
            case 8:
                task9()
