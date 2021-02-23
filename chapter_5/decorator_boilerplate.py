"""
This module defines a boilerplate for writing complex decorators
"""

import functools

def decorator(func):
    """This is the decorator
    """
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before executing decorated function
        print("Decoration before..")
        value = func(*args, **kwargs)
        # Do something after executing decorated function
        print("Decoration after..")
        return value
    return wrapper_decorator


@decorator
def say_hello(name):
    """This function is for testing the decorator
    """
    return f"Hello {name}"

if __name__ == '__main__':
    GREET = say_hello("Faruk")
    print(GREET)
