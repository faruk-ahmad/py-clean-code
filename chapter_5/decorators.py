"""
This module defines some decorators for reusability
"""

def do_twice(func):
    """This decorator executes func twice
    """
    def wrapper_do_twice(*args, **kwargs):
        """Adding *args and **kwargs will allow
        decorating func whether there is any argument
        passed or not.
        """
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
