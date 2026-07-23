#####################################################
# CS03A - Summer 2026
# Lab 4 - Challenge 1: Total Sales / Date Printer
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################

from datetime import datetime

def get_valid_sales_figure(prompt: str) -> float:
    """
    Loops until user inputs a valid float
    """
    while True:
        user_input = input(prompt).strip()
        try:
            number = float(user_input)

            # Check if the number is non-negative
            if number >= 0:
                return number
            else:
                print("X Invalid input: Sales figure cannot be negative.")
        except ValueError:
            print(f"X Invalid input: '{user_input}'. Please enter a valid numerical amount.")

def get_valid_date(prompt: str) -> str:
    """Loops until the user enters a valid date in mm/dd/yyyy format."""
    while True:
        user_input = input(prompt).strip()
        try:
            # Parses the string according to the strict format
            datetime.strptime(user_input, "%m/%d/%Y")
            return user_input
        except ValueError:
            print("X Invalid date or format. Please use mm/dd/yyyy (e.g., 03/12/2018).")

def calculate_total_sales():
    days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    sales_for_week = []
    total_sales = 0

    for day in days_of_the_week:
        daily_sales = get_valid_sales_figure(f"Enter sales numbers for {day}: ")
        sales_for_week.append(daily_sales)

    for sale in sales_for_week:
        total_sales += sale

    print(f"Total Weekly Sales: ${total_sales:.2f}")


def date_printer():

   
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    date_str = get_valid_date("Enter a date (mm/dd/yyyy): ")

    # Split the string by '/' and unpack into variables
    month_str, day_str, year_str = date_str.split('/')

    # Convert string values to integers to handle leading zeros (i.e. "03" -> 3)
    month_num = int(month_str)
    day_num = int(day_str)
    
    month_name = months[month_num - 1]

    print(f"{month_name} {day_num}, {year_str}")


if __name__ == "__main__":
    print("************* LAB 4 **************")
    print("********** Challenge 1 ***********")
    print("** Calculate Weekly Sales Total **")
    calculate_total_sales()
    print("********** Date Printer ***********")
    date_printer()