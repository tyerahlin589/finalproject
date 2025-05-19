def greet(name):
    if name == "Alice":
        print("Hello Alice!")
    elif name == "Bob":
        print("Hello Bob!")
    else:
        print(f"Hello {name.capitalize()}!")

greet("Alice")
greet("Bob")
