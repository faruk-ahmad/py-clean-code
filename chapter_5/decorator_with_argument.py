"""
This module defines a boilerplate for writing complex decorators
with arguments passed to the decorator.
"""

import functools

def repeat(_func=None, * , num=3):
    """This is the decorator with argument
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            # Do something before executing decorated function
            print("Decoration before..")
            value = []
            for _ in range(num):
                value.append(func(*args, **kwargs))
            # Do something after executing decorated function
            print("Decoration after..")
            return value
        return wrapper_decorator
    if _func is None:
        return decorator
    return decorator(_func)


@repeat(num=7)
def say_hello(name):
    """This function is for testing the decorator
    """
    return f"Hello {name}"

if __name__ == '__main__':
    GREET = say_hello("Faruk")
    print(GREET)