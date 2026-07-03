#####################################################
# CS03A - Summer 2026
# Assignment 1 - Question 4: Tuition Increase
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################

def run():
    """Calculates and displays projected semester tuition changes over a 5-year timeline."""
    tuition = 8000.00
    annual_tuition_increase = 1.03 # 3% increase
    number_of_years = 5

    print("Projected Semester Tuition for the Next 5 Years:")
    print("-" * 30)
    for i in range(1, number_of_years + 1):
        tuition *= annual_tuition_increase
        print(f"Year {i} Tuition: ${tuition:,.2f}")


if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q4.py`)
    run()