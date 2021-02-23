"""
This module shows how to return a function
from inside of another function.
"""

def parent(num):
    """This function returns the inner function
    based on the value of num.
    """

    def first_child():
        return "I am first child."

    def second_child():
        return "I am second child"

    if num == 1:
        return first_child
    return second_child


if __name__ == '__main__':
    first = parent(1)
    second = parent(2)
    print(first)
    print(first())
    print(second)
    print(second())
