"""
This module shows how to use a function as
argument to another function.
"""

def hello(name):
    """Returns the valus of name
    """
    return f"Hello {name}"

def awesome(name):
    """Returns the value of name with extra
    """
    return f"Hi, {name}, nice to meet you."

def greet(greeter_func):
    """Returns msg from greeter func with extra
    """
    return f"{greeter_func('Faruk')}. How are you?"


if __name__ == '__main__':
    NAME = "Ahmad"
    print(hello(NAME))
    print(awesome(NAME))
    print(greet(awesome))
    print(greet(hello))