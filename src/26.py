def calculate_square_root(number):
    if number < 0:
        raise ValueError("Square root of a negative number is not defined.")
    
    square_root = number ** 0.5
    return square_root

try:
    result = calculate_square_root(16)
    print(f"The square root of 16 is: {result}")
except ValueError as e:
    print(e)

result = calculate_square_root(-4)
print(f"The square root of -4 is: {result}")
