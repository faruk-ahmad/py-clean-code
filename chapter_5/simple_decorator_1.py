"""
This module shows how a simple decorator works.
"""

def my_decorator(func):
    """This function defines a wrapper function.
    """
    def wrapper():
        print("Something before calling func.")
        func()
        print("Something after calling func.")

    return wrapper

def say_hurrah():
    """say hurrah
    """
    print("Hurrah")

if __name__ == '__main__':
    say_hurrah = my_decorator(say_hurrah)
    say_hurrah()
