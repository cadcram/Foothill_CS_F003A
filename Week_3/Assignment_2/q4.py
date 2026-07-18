#####################################################
# CS03A - Summer 2026
# Assignment 2 - Question 4: Personal Web Page Generator
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################
import os

def generate_webpage(name: str, description: str) -> str:
    """
    Create an HTML file containing a personal webpage with a name 
    and description, then return its absolute path.

    Args:
        name (str): The name to be displayed as the main heading.
        description (str): A sentence or paragraph describing the person.

    Returns:
        str: The absolute file path of the generated HTML webpage.
    """
    file_name = 'webpage.html'
    html_content = f"""<html>
                        <head>
                        </head>
                        <body>
                        <center>
                        <h1>{name}</h1>
                        </center>
                        <hr />
                        {description}
                        </body>
                        </html>"""
    try:
        outfile = open(file_name, 'w')
        outfile.write(html_content)
        outfile.close()

        # Get the absolute path of the file
        absolute_path = os.path.abspath(file_name)

        return absolute_path
    except IOError:
        print("Error: Could not write the file to disk. Check your permissions.")
        return "ERROR"

    

def run():
    """
    1. Prompts the user to input name and self description to put on the webpage
    2. Calls generate_webpage to create html file
    3. Prints out path to new file
    """
    print("Welcome to the Personal Web Page Generator")
    name = input("Enter your name: ")
    description = input("Describe yourself: ")

    new_webpage_path = generate_webpage(name, description)

    # Display path of new file to the user
    print(f"Success! Your webpage has been saved to:\n{new_webpage_path}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()    