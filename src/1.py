import random

def get_random_code(length=8):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    special_characters = '!@#$%^&*()-=+{}[]:;"\\|'
    code = ''
    for i in range(length):
        code += random.choice(letters)
        code += random.choice(numbers)
        code += random.choice(special_characters)
    return code