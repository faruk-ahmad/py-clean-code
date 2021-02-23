"""
This module defines some decorators for reusability
"""

import functools

def do_twice(func):
    """This decorator executes func twice
    """
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        """Adding *args and **kwargs will allow
        decorating func whether there is any argument
        passed or not.
        """
        return func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
