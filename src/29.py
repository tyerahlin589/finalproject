import numpy as np

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    
    # Initialize the first two numbers in the Fibonacci sequence
    fib1, fib2 = 0, 1
    
    # Calculate the sum of the first 'n' terms (fibonacci number)
    for _ in range(n):
        if not isinstance(_, int) or not isinstance(_, float):
            raise TypeError("The input should be a positive integer.")
        
        n_elements = len(fib1 + fib2)
        if n > 0:
            return str(sum(fib1 + fib2))
        else:
            return "Sum is already calculated."
