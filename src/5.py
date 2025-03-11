import numpy as np

def get_unique_elements(my_list):
    return list(set(my_list))

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7]
    print(get_unique_elements(my_list))