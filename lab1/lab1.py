def main() -> None:
    # - write a program that prints hello world
    print("Hello, world")

    # - application to take a number in binary form from the user, and print it as a decimal
    number = input("Enter a binary number: ")
    while not all(digit in ["0", "1"] for digit in number):
        number = input("Enter a valid binary number: ")

    print(int(number, 2))

    # - write a function that takes a number as an argument and if the number
    # 	divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
    # 	divisible by both return "FizzBuzz"
    def fizz_buzz(n: int) -> str:
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return ""

    num = input("Enter a number to play fizz buzz: ")
    while not (("1" <= num[0] <= "9") and all("0" <= d <= "9" for d in num[1:])):
        num = input("Enter a number to play fizz buzz: ")

    print(fizz_buzz(int(num)))

    # - Ask the user to enter the radius of a circle print its calculated area and circumference
    rad = int(input("Enter the circle raduis: "))
    PI = 3.14
    print(f"circumference: {round(2 * rad * PI, 2)}")
    print(f"area: {round((rad**2) * PI, 3)}")

    # - Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
    def validate_user_data() -> None:
        name = input("Enter your name: ")
        while not (name and name.strip().isalpha()):
            name = input("Enter a valid name: ")

        email = input("Enter your email: ")

        def is_valid_email(em: str) -> bool:
            em = em.strip()
            at_sign_idx = em.rfind("@")
            dot_sign_idx = em.rfind(".")

            # simulate --> test@domain.(com | gov)
            return (
                em
                and (
                    dot_sign_idx != -1
                    and at_sign_idx != -1
                    and dot_sign_idx - at_sign_idx >= 2  # letters in between @ and .
                    and em[dot_sign_idx + 1 :] in ["com", "gov", "org"]
                )
            )

        while not is_valid_email(email):
            email = input("Enter a valid email: ")

        print(f"name: {name}\nemail: {email}")

    validate_user_data()

    # - Write a program that prints the number of times the substring 'iti' occurs in a string
    def count_iti(s: str) -> int:
        return s.count("iti")

    word = input("Enter a word to count occurances of 'iti' in it: ")
    print(f"iti count: {count_iti(word)}")


if __name__ == "__main__":
    main()
