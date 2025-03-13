import random 
def get_random_word(length): 
    word = "" 
    for i in range(length): 
        word += chr(ord('a') + random.randint(0, 25)) 
    return word 

def main(): 
    print(get_random_word(10)) 

main()