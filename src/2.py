import random

def get_random_code():
    """Returns a randomly generated code"""
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_chars = "@#$%^&*()_+-=[]{}|;':\"<>,./?`~"

    code = ""
    for i in range(10):
        code += random.choice(letters)
    for i in range(4):
        code += random.choice(numbers)
    for i in range(2):
        code += random.choice(special_chars)

    return code