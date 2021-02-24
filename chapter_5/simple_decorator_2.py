"""
This module shows how to use decorator
in python in pythonic way.
"""

def my_decorator(func):
    """This is a python function that
    works as a decorator.
    """
    def wrapper():
        print("Before calling decorated function.")
        func()
        print("After calling decorated function.")
    return wrapper

@my_decorator
def say_hurrah():
    """ Say hurrah
    """
    print("Hurrah")


if __name__ == '__main__':
    say_hurrah()
