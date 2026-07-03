#####################################################
# CS03A - Summer 2026
# Assignment 1 - Question 2: Magic Dates
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################

def get_valid_date_input(date_type: str, lower_bound: int, upper_bound: int) -> int:
    """Ensures user inputs the correct month/day/year range.

    Parameters:
    date_type (str): Should be Month, Day, or Year to generate the input prompt
    lower_bound (int): Lowest value for a date range
    upper_bound (int): Highest value for a date range

    Returns:
    int: The validated date value within the specified bounds
    """
    
    # Keep asking for value until valid value is given
    while True:
        # Get the input from the user specificing day/month/year and valid entry bounds
        user_input = input(f"Enter a {date_type} between {lower_bound} and {upper_bound}: ")

        try:
            # Convert the string input to a int for numeric comparison
            number = int(user_input)
            
            # Check if the number is within the range (Inclusive Check)
            if lower_bound <= number <= upper_bound:
                return number
            else:
                print(f"Error: {number} is outside the range.")
                continue
                
        except ValueError:
            # Handles cases where the user types letters instead of numbers
            print("Invalid input! Please enter a valid number.")
            continue

def validate_month_day(month: int, day: int) -> bool:
    """Validates selected day is a vaild day in the selected month.

    Parameters:
    month (int): user inputted month
    day (int): user inputted day

    Returns:
    bool: if the day is in the month
    """
    
    # Dictionary mapping month number to maximum days (setting February to 28)
    # Does not factor in leap years because cannot determine that with two digit year (i.e. 00 could be 1900, 2000, 2100)
    days_in_months = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Check if month is valid, then check if day is in range
    if month in days_in_months:
        return 1 <= day <= days_in_months[month]
        
    return False

def run():
    print("Give me a month, day and a year and I will tell you if it is ***MAGIC***")

    month = get_valid_date_input("month", 1, 12)
    day = get_valid_date_input("day", 1, 31)

    # Validate that month-day combinition is valid
    is_valid_date = validate_month_day(month, day)

    if not is_valid_date and day == 29 and month == 2:
        leap_year_response = input("Is this a leap year? Yes or No (Tell the truth!): ")
        if leap_year_response == "Yes":
            is_valid_date = True  # Override flag because it's a valid leap day

    # If it's still not a valid date, exit the program
    if not is_valid_date:
        print("That is not a valid date on the calendar. Try again later!")
        return

    year = get_valid_date_input("year", 0, 99)

    month_day_product = month * day

    if month_day_product == year:
        print(f"This date ({month}/{day}/{year}) is ***MAGIC***.")
    else:
        print(f"This date ({month}/{day}/{year}) is ***NOT*** magic. :(")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q2.py`)
    run()