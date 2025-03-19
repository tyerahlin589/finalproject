import random

def get_random_code(length=10):
    """Generates a random string of letters and digits of the length provided."""
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    characters = letters + numbers
    result = ''
    for i in range(length):
        result += random.choice(characters)
    return result