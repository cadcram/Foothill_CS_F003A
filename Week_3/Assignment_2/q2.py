#####################################################
# CS03A - Summer 2026
# Assignment 2 - Question 2: Prime Number Generation
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################

def get_integer_greater_than_one(prompt: str) -> int:
    """
    Keeps prompting the user until they enter an integer greater than 1.
    """
    while True:
        try:
            value = int(input(prompt))
            # Force user to enter integer greater to 1 since 1 is not prime
            if value > 1: 
                return value
            print("Error: The number must be greater than 1.")
        except ValueError:
            print("Error: That is not a valid integer.")

def is_prime(num: int) -> bool:
    """
    Determines if a number is prime using division up to sqrt(num).
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def display_prime_status(num: int):
    """
    Accepts an integer and displays it only if it is a prime number.
    """
    if is_prime(num):
        print(num)

def run():
    """
    Drives the prime number generation program.
    """
    print("Welcome to the Prime Number Generator!")
    limit = get_integer_greater_than_one("Please enter an integer greater than 1: ")

    # Populate a list with integers from 2 up through the value entered
    num_list = []
    for i in range(2, limit + 1):
        num_list.append(i)
    
    # Header formatting
    print("-" * 40)
    print(f"Prime numbers from 2 to {limit}:")
    print("-" * 40)

    # Step through the list and pass each element to the display function
    for num in num_list:
        display_prime_status(num)

if __name__ == "__main__":
    run()