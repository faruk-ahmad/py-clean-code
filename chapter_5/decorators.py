"""
This module defines some decorators for reusability
"""

def do_twice(func):
    """This decorator executes func twice
    """
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
