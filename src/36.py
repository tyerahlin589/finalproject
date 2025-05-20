def square_numbers(numbers):
    result = []
    for number in numbers:
        squared_number = number ** 2
        result.append(squared_number)
    return result

numbers = [1, 2, 3, 4]
squares = square_numbers(numbers)

print(squares)
