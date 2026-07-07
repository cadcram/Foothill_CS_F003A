#####################################################
# CS03A - Summer 2026
# Lab 2 - Challenge 1: Age Classifier / Calories Burned
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################

def get_valid_number(prompt: str) -> int:
    """Prompts the user for input and ensures it is a non-negative whole integer.

    This function loops continuously, trapping string-to-integer conversion 
    errors and rejecting negative numbers until a physically valid age is provided.

    Parameters:
        prompt (str): The text message displayed to the user requesting input.

    Returns:
        int: A validated, non-negative integer representing the user's age.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            number = int(user_input)

            # Check if the number is positive
            if number >= 0:
                return number
            else:
                print("X Invalid input: Number must be greater than zero.")
        except ValueError:
            print(f"X Invalid input: '{user_input}'. Please enter a whole number.")

def age_classifier():
    """Prompts for a person's age and classifies them into a life stage.

    Evaluates the validated integer input against specific threshold brackets 
    to determine and display whether the individual is categorized as an 
    infant, a child, a teenager, or an adult based on prompt rules.
    """
    print("*" * 30)
    print("WELCOME TO THE AGE CLASSIFIER")
    print("*" * 30)

    age = get_valid_number("Please enter your age: ")
    verdict = "UNK"

    # Classify the age into developmental life stages based on prompt brackets
    if age <= 1:
        verdict = "an infant"
    elif 1 < age < 13:
        verdict = "a child"
    elif 13 <= age < 20:
        verdict = "a teenager"
    else:
        verdict = "an adult"

    print(f"You are {verdict}.")


def calories_burned():
    """Calculates and displays a breakdown of cumulative calories burned over time.

    Uses an iterative loop running at fixed 5-minute increments to project 
    the total energy expenditure of running on a treadmill calibrated to a 
    burn rate of 4.2 calories per minute.
    """
    print("*" * 30)
    print("****** Calories Burned ******")
    print("*" * 30)

    CALORIES_PER_MINUTE = 4.2

    # Loop from 10 to 30 minutes (inclusive) at 5-minute intervals
    for time in range(10,31,5):
        calories_burned = CALORIES_PER_MINUTE * time
        print(f"{time} minutes: You have burned {calories_burned:.1f} calories.")





if __name__ == "__main__":
    age_classifier()
    print("\n")
    calories_burned()