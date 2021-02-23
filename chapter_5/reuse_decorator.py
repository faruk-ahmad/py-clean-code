"""
This module show how to reuse decorators
"""

from decorators import do_twice

@do_twice
def say_hurrah():
    """Say hurrah
    """
    print("Hurrah!")

if __name__ == '__main__':
    say_hurrah()
