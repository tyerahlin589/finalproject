import random

def random_python_code():
    # Generate a random number between 1 and 5
    num = random.randint(1, 5)

    # Check if the number is even or odd
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Call the function
random_python_code()