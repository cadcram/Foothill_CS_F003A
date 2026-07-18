#####################################################
# CS03A - Summer 2026
# Assignment 2 - Question 1: Falling Distance
# Student Name: Caden Cramsey
# SID: 20750632
#####################################################

# Standard acceleration due to gravity on Earth (m/s²)
GRAVITY = 9.8

def falling_distance(time: float) -> float:
    """Calculates and returns the falling distance in meters using d = 1/2gt²."""
    distance = 0.5 * GRAVITY * (time ** 2)
    return distance


def run():
    """
    Calls falling_distance in a loop from 1 to 10 seconds 
    and displays the returned values.
    """
    print(f"{'Time (seconds)':<15}| {'Distance Fallen (meters)':<25}")
    print("-" * 40)
    
    for seconds in range(1, 11):
        # Capture the returned value from the function
        distance = falling_distance(seconds)
        
        # Display the returned value
        print(f"{seconds:^15}|{distance:^25.2f}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()