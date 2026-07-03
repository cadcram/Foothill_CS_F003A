#####################################################
# CS03A - Summer 2026
# Assignment 1 - Question 3: Time Calculator
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################

import re

def get_pure_integer(prompt: str) -> int:
    """Prompts the user for input and ensures it contains only numeric digits.

    Parameters:
        prompt (str): The text displayed to the user requesting input.

    Returns:
        int: The validated integer containing only digits.
    """
    while True:
        user_input = input(prompt).strip()

        # Regex enforces that the entire string consists strictly of digits (0-9)
        if re.match(r'^\d+$', user_input):
            return int(user_input)
        else:
            print(f"X Invalid input: '{user_input}'. Input must contain only numbers.")

def plural(number: int, unit: str) -> str:
    """Formats a time unit string with proper singular or plural grammar.

    Parameters:
        number (int): The count of the specific time unit.
        unit (str): The base singular name of the unit (i.e. 'day', 'hour').

    Returns:
        str: A string combining the number and correctly inflected unit name.
    """
    result = f"{number} {unit}"
    if number != 1:
       result += "s"
    return result

def run():
    """
    Executes the core time calculator application logic.
    """

    # Constants for seconds in other unit of time
    SECONDS_IN_DAY = 86400
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    print("Hi, welcome to the Time Calculator where you can give any number of seconds and I will convert it to days, hours, minutes, and seconds")
    number = get_pure_integer("Enter a number of seconds: ")

    # Sequentially break down total seconds into largest possible whole time units
    days = number // SECONDS_IN_DAY
    number = number % SECONDS_IN_DAY

    hours = number // SECONDS_IN_HOUR
    number = number % SECONDS_IN_HOUR

    minutes = number // SECONDS_IN_MINUTE
    seconds = number % SECONDS_IN_MINUTE

    # Dynamically build the output string
    if days >= 1:
        result = f"{plural(days, 'day')}, {plural(hours, 'hour')}, {plural(minutes, 'minute')}, {plural(seconds, 'second')}"
    elif hours >= 1:
        result = f"{plural(hours, 'hour')}, {plural(minutes, 'minute')}, {plural(seconds, 'second')}"
    elif minutes >=1:
        result = f"{plural(minutes, 'minute')}, {plural(seconds, 'second')}"
    else:
        result = f"{plural(seconds, 'second')}"

    print(result)

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q3.py`)
    run()