#####################################################
# CS03A - Summer 2026
# Assignment 2 - Question 3: Sentence Capitalizer
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################

def sentence_formatter(user_string: str) -> str:
    """
    Take in a string and loop through characters and build modified string with
    proper capitalization and spacing.

    Args:
        user_string (str): String from user to be formatted.

    Returns:
        str: String with proper capitalization and spacing.
    """
    capitalize_next = True
    modified_text = ""

    # FIXED: Changed len(input) to len(user_string) to avoid crash
    for i in range(len(user_string)):
        current_char = user_string[i]

        # Check if char is punctuation
        if current_char in ".?!":
            modified_text += current_char
            # If punctuation, then next alphabetic char should be capitalized
            capitalize_next = True
            
            # Check if at end of user_string to avoid index error
            # and if next char is a space to determine if space is needed
            if i + 1 < len(user_string) and user_string[i + 1] != " ":
                modified_text += " "
        # If capitalized_next state is true and char is alphabetic
        # then capitalize
        elif capitalize_next and current_char.isalpha():
            modified_text += current_char.upper()
            capitalize_next = False
        else:
            # If the current character is a space, only add it if the 
            # LAST character we added wasn't already a space.
            if current_char == " ":
                if len(modified_text) > 0 and modified_text[-1] != " ":
                    modified_text += current_char
            else:
                modified_text += current_char
    return modified_text

def run():
    """
    1. Prompt user to input a string
    2. Modify string with proper capitalization and spacing
    3. Print modified string
    """
    print("Welcome to the Sentence Capitalizer.")
    input_string = input("Enter your sentence(s): ")

    mod_string = sentence_formatter(input_string)

    print(mod_string)

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()