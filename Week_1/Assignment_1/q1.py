#####################################################
# CS03A - Summer 2026
# Assignment 1 - Question 1: Compound Interest
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################
import re

def get_number_with_regex(prompt: str) -> float:
    """Cleanses input text to parse a floating point or integer number.

    Parameters:
        prompt (str): The text message displayed to the user.

    Returns:
        float: The extracted numeric value.
    """
    while True:
        user_input = input(prompt)

        # Strip out all inputs except digits and decimals
        cleaned_input = re.sub(r'[^0-9.]','', user_input)

        # Handle Edge Case: No number at all i.e 'abc'
        if not cleaned_input:
            print(f"X Invalid input: '{user_input}'. No numbers found.")
            continue

        try:
            # If there is a decimal, return a float otherwise return int
            if '.' in cleaned_input:
                return float(cleaned_input)
            return int(cleaned_input)
        except ValueError:
            # Catches value with more than one decimal point i.e. '12.34.56'
            print(f"X Invalid input: '{user_input}'. Could not parse as a clean number.")


def calculate_account_amount(p: float, r: float, n: float, t: float) -> float:
    """
    Calculates the amount of money in account after a specified number of years
    
    Parameters:
    p (float): principal amount originally deposited into the account (as a float, i.e 100 for $100 or 250.50 for $250.25)
    r (float): annual interest rate paid by the account (as a float, i.e 5 for 5% or 2.5 for 2.5%)
    n (float): number of times per year that the interest is compounded (i.e. if
               interest is compounded monthly, enter 12. If interest is compounded quarterly,
               enter 4.)
    t (float): number of years the account will be left to earn interest (as a float, i.e. 2.5 years)

    Returns:
        float: Calculated final account balance.
    """
    adjusted_rate = r / 100
    amount = p * (1 + adjusted_rate / n) ** (n * t)
    return amount

def run():
    print("Welcome to the Compound Interest Calculator!")
    print("Allow me to ask you a few questions to calculate the amount in your account after interest.")
    print("-" * 30)

    # Get all values needed to calculate account after interest (Values will be cleaned from user input)
    principal = get_number_with_regex("Enter your initial principal: ")

    rate = get_number_with_regex("Enter the annual interest rate of account in percent "
                                 "(i.e 5 for 5% or 2.5 for 2.5%): ")
    
    number_compounded = get_number_with_regex("Enter the number of times per year that the interest is compounded \n"
                                               "(i.e. if interest is compounded monthly, enter 12. If interest is compounded quarterly, 4.): ")
    
    time_in_account = get_number_with_regex("Enter number of years the account will be left to earn interest: ")

    # Calculated final account balence after accruing interest with cleaned values
    final_amount = calculate_account_amount(principal, rate, number_compounded, time_in_account)

    print("-" * 30)
    print(f"Final Amount: ${final_amount:,.2f} ")



if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
