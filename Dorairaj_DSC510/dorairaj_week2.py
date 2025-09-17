# DSC 510
# Week 2
# Programming Assignment Week 2
# Author: Ravi Dorairaj
# Date: 09/16/2025
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
# Change(s) Made: Added error handling to check for invalid (non-numeric) input, added some comments to improve readability
# Date of Change: 09/16/2025
# Author: Ravi Dorairaj
# Change Approved by: Instructor
# Date Moved to Production: 09/16/2025
# --------------------------------------------------------

# Welcome message before we get input from customer
print("Welcome to the Fiber Optic Installation Cost Calculator!")

# Retrieve user input for company name
company_name = input("Please enter your company name: ")

# Retrieve number of feet of fiber optic cable
# Validate so only numeric input is accepted
while True:
    user_input = input("Enter the number of feet of fiber optic cable to be installed: ")
    if user_input.replace(".", "", 1).isdigit():
        feet_requested = float(user_input)
        break
    else:
        print("❌ Invalid input. Please enter a numeric value.")

# Define cost per foot
# Added constant file for cost per foot and declared after validation for better memory management
COST_PER_FOOT = 0.95

# Calculate total installation cost
total_cost = feet_requested * COST_PER_FOOT

# Print a formatted receipt
print("\n----- Installation Receipt -----")
print(f"Company Name: {company_name}")
print(f"Feet of Fiber Optic Cable: {feet_requested:,.2f} ft")
print(f"Cost per Foot: ${COST_PER_FOOT:.2f}")
print(f"Total Installation Cost: ${total_cost:,.2f}")
print("--------------------------------")
print("Thank you for choosing our service!")