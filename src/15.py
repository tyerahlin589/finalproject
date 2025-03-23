import random

def get_random_integers(min_num: int = 0, max_num: int = 10):
    """
    Generate a list of 'max_num' integers between 'min_num' and 'max_num'.
    
    Parameters:
    min_num (int): The minimum value for the generated numbers.
    max_num (int): The maximum value for the generated numbers.
    
    Returns:
    list: A list of random integers generated within the specified range.
    """
    return [random.randint(min_num, max_num) for _ in range(random.randint(1, 10))]
