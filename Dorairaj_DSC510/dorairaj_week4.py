# DSC 510
# Week 4
# Programming Assignment Week 4
# Author: Ravi Dorairaj
# Date: 10/02/2025
#
# Program: Fiber Optic Installation Cost Calculator with Discounts & Functions
# Purpose:
#   Calculate installation cost for fiber optic cable using bulk discounts.
#   Program demonstrates functions, main method, and proper structure.
#   Prompts for company name and feet required, validates input, applies tiered
#   pricing, calls a dedicated cost calculation function, and prints a receipt.
#
# Change Control Log:
# Change#: 6
# Change(s) Made:
#   1) Added aligned receipt formatting for readability.
#   2) Improved docstrings for clarity.
#   3) Added type hints in main.
#   4) Confirmed pricing tiers with edge case tests.
# Date of Change: 10/04/2025
# Author: Ravi Dorairaj
# Change Approved by: Instructor
# Date Moved to Production: 10/04/2025
# --------------------------------------------------------

"""Week 4 — Fiber Optic Installation Cost Calculator with Functions and Main."""

# Pricing tiers (per foot)
PRICE_BASE = 0.95       # up to and including 100 ft
PRICE_101_250 = 0.85    # > 100 ft up to 250
PRICE_251_500 = 0.75    # > 250 ft up to 500
PRICE_OVER_500 = 0.55   # > 500 ft


def determine_price_per_foot(feet: float) -> float:
    """Return price per foot based on bulk discount tiers."""
    if feet > 500:
        return PRICE_OVER_500
    elif feet > 250:
        return PRICE_251_500
    elif feet > 100:
        return PRICE_101_250
    else:
        return PRICE_BASE


def calculate_cost(feet: float, price_per_foot: float) -> float:
    """Return total installation cost given cable length (feet) and rate."""
    return feet * price_per_foot


def get_company_name() -> str:
    """Prompt the user for a non-empty company name."""
    company = ""
    while not company:
        company = input("Please enter your company name: ").strip()
        if not company:
            print("Company name cannot be blank.\n")
    return company


def get_feet_requested() -> float:
    """Prompt the user for feet input with validation (must be > 0)."""
    while True:
        raw = input("Enter the number of feet to be installed: ").strip()
        try:
            feet = float(raw)
            if feet <= 0:
                print("Invalid input. Please enter a number greater than 0.\n")
                continue
            return feet
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")


def print_receipt(company: str, feet: float, price: float, total: float) -> None:
    """Print the formatted installation receipt."""
    print("\n----- Installation Receipt -----")
    print(f"{'Company Name':<22}: {company}")
    print(f"{'Feet of Cable Ordered':<22}: {feet:,.2f} ft")
    print(f"{'Price per Foot':<22}: ${price:.2f}")
    print(f"{'Total Installation':<22}: ${total:,.2f}")
    print("--------------------------------")
    print("Thank you for     your business.")


def main() -> None:
    """Run the calculator by orchestrating helper functions."""
    print("Welcome to the Fiber Optic Cable Installation Cost Calculator.\n")

    company_name = get_company_name()
    feet_requested = get_feet_requested()
    price_per_foot = determine_price_per_foot(feet_requested)
    total_cost = calculate_cost(feet_requested, price_per_foot)

    print_receipt(company_name, feet_requested, price_per_foot, total_cost)


# Program entry point
if __name__ == "__main__":
    main()