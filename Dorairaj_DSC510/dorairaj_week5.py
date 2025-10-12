# DSC 510
# Week 5
# Programming Assignment Week 5
# Author: Ravi Dorairaj
# Date: 10/08/2025
#
# Program: Mathematical Operations & Average Calculator with Loops and Functions
# Purpose:
#   Demonstrate the use of loops and functions in Python by performing
#   various mathematical operations (+, -, *, /) and computing averages
#   for a user-provided list of numbers.
#   Program runs continuously using a while loop until the user chooses to exit.
#
# Change Control Log:
# Change#: 3
# Change(s) Made:
#   1) Implemented perform_calculation() with error handling.
#   2) Implemented calculate_average() using for loop.
#   3) Added separate run_program_loop() method to keep main() clean.
# Date of Change: 10/08/2025
# Author: Ravi Dorairaj
# Change Approved by: Instructor
# Date Moved to Production: 10/08/2025
# --------------------------------------------------------

"""Week 5 — Demonstrate loops and functions with math and averaging operations."""


def perform_calculation(operation: str) -> float:
    """
    Perform the specified mathematical operation on two numbers.
    :param operation: One of '+', '-', '*', '/'
    :return: Result of the calculation
    """
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Division by zero is not allowed.")
                return None
            result = num1 / num2
        else:
            print("Invalid operation.")
            return None

        return result

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None


def calculate_average() -> float:
    """
    Prompt the user for a number of values and compute their average using a for loop.
    :return: The calculated average
    """
    try:
        count = int(input("How many numbers would you like to average? "))
        if count <= 0:
            print("Please enter a number greater than zero.")
            return None

        total = 0.0
        for i in range(1, count + 1):
            while True:
                try:
                    value = float(input(f"Enter number {i}: "))
                    total += value
                    break
                except ValueError:
                    print("Please enter a valid numeric value.")

        average = total / count
        return average

    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None


def run_program_loop() -> None:
    """
    Main program loop. Allows user to perform calculations or averages repeatedly
    until they choose to exit.
    """
    print("Welcome to the Python Math & Average Calculator!")
    print("You can perform addition, subtraction, multiplication, division, or compute an average.\n")

    while True:
        print("Select an option:")
        print("1. Perform a mathematical calculation (+, -, *, /)")
        print("2. Calculate an average")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            operation = input("Enter the operation (+, -, *, /): ").strip()
            result = perform_calculation(operation)
            if result is not None:
                print(f"Result of {operation} operation: {result:.2f}\n")

        elif choice == '2':
            avg = calculate_average()
            if avg is not None:
                print(f"The calculated average is: {avg:.2f}\n")

        elif choice == '3':
            print("Thank you for using the calculator. Goodbye!")
            break

        else:
            print("Invalid selection. Please enter 1, 2, or 3.\n")


def main() -> None:
    """Program entry point — calls the main loop function."""
    run_program_loop()


# Program entry point
if __name__ == "__main__":
    main()