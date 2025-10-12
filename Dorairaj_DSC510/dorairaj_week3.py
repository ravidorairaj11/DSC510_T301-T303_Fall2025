# DSC 510
# Week 2
# Programming Assignment Week 2
# Author: Ravi Dorairaj
# Date: 09/17/2025
#
# Program: Fiber Optic Installation Cost Calculator
# Purpose:
#   This program calculates the installation cost of fiber
#   optic cable for a company. It accepts user input for
#   the company name and the number of feet of fiber optic
#   cable to be installed, then generates a receipt with
#   the calculated total cost.
#
# Change Control Log:
# Change#: 2
# Change(s) Made:
# 1) Added error handling to check for invalid (non-numeric) input
# 2) Added some comments to improve readability
# Date of Change: 09/17/2025
# Author: Ravi Dorairaj
# Change Approved by: Instructor
# Date Moved to Production: 09/17/2025
# --------------------------------------------------------

"""Week 2 — Fiber Optic Installation Cost Calculator."""

COST_PER_FOOT = 0.95  # PEP 8: constants in ALL_CAPS


def main() -> None:
    """Run the interactive calculator and print a receipt."""
    print("Welcome to the Fiber Optic Installation Cost Calculator!")

    company_name = input("Please enter your company name: ").strip()

    # Numeric validation using float() for robustness (handles 1e3, .5, spaces, etc.)
    while True:
        user_input = input("Enter the number of feet of fiber optic cable to be installed: ").strip()
        try:
            feet_requested = float(user_input)
            # Optional: enforce non-negative values
            if feet_requested < 0:
                print("Invalid input. Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    total_cost = feet_requested * COST_PER_FOOT

    print("\n----- Installation Receipt -----")
    print(f"Company Name: {company_name}")
    print(f"Feet of Fiber Optic Cable: {feet_requested:,.2f} ft")
    print(f"Cost per Foot: ${COST_PER_FOOT:.2f}")
    print(f"Total Installation Cost: ${total_cost:,.2f}")
    print("--------------------------------")
    print("Thank you for choosing our service!")

if __name__ == "__main__":
    main()