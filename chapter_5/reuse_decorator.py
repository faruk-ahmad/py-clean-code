"""
This module show how to reuse decorators
"""

from decorators import do_twice

@do_twice
def say_hurrah():
    """Say hurrah
    """
    print("Hurrah!")

@do_twice
def say_hamba(name):
    """Say hamba
    """
    print("Saying Hamba-")
    return f"Hello- {name}"

if __name__ == '__main__':
    print(say_hurrah())
    print(say_hamba("World"))
