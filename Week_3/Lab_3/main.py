#####################################################
# CS03A - Summer 2026
# Lab 3 - Challenge 1: Stadium Seating
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################

'''
There are three seating categories at a stadium. 
Class A seats cost $20
Class B seats cost $15
Class C seats cost $10. 

Write a function that takes in the number of tickets for each class of seats were sold, 
then displays the amount of income generated from ticket sales.

In your program, write the main function and calling your newly created function in the main function
'''
import time

# Ticket prices per class
CLASS_A_PRICE = 20
CLASS_B_PRICE = 15
CLASS_C_PRICE = 10

def get_valid_number(prompt: str) -> int:
    """Prompts the user for input and ensures it is a non-negative whole integer."""
    while True:
        user_input = input(prompt).strip()
        try:
            number = int(user_input)

            # Check if the number is positive or 0
            if number >= 0:
                return number
            else:
                print("X Invalid input: Number must be 0 or greater.")
        except ValueError:
            print(f"X Invalid input: '{user_input}'. Please enter a whole number.")

def gather_ticket_orders():

    ticketA = get_valid_number("Enter number of Class A tickets sold: ")
    ticketB = get_valid_number("Enter number of Class B tickets sold: ")
    ticketC = get_valid_number("Enter number of Class C tickets sold: ")

    return ticketA, ticketB, ticketC

def calculate_ticket_revenue(ticketA: int, ticketB: int,ticketC: int) -> int:
    
    # Calculate individual class revenue
    revenue_a = CLASS_A_PRICE * ticketA
    revenue_b = CLASS_B_PRICE * ticketB
    revenue_c = CLASS_C_PRICE * ticketC

    # Calculate total revenue
    revenue =  revenue_a + revenue_b + revenue_c

    return revenue


if __name__ == "__main__":
    print("Hi, welcome to the ticket income generator.")

    # Gather ticket sales per class
    ticket_a, ticket_b, ticket_c = gather_ticket_orders()

    # Calculate ticket revenue based on inputs
    revenue = calculate_ticket_revenue(ticket_a, ticket_b, ticket_c)

    # Add fun status to make the user thing the computer is working really hard
    print("Calculating", end="", flush=True)

    # Loop for 1 seconds (printing one dot every 0.1 seconds)
    for i in range(10):
        time.sleep(0.1)
        print(".", end="", flush=True)

    print("Done!")

    time.sleep(0.5)

    # Print calculated revenue from inputs
    print(f"Revenue Generated from Ticket Sales: ${revenue}")