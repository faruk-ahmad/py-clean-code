"""
This module defines some mathematical operations.
"""


def add(number_1:int, number_2:int) -> int:
    """ A function to add two numbers.

    This function takes two number as input and
    return the summation of those two numbers.

    Args:
        number_1: first integer number to be added
        number_2: second integer number to be added

    Returns:
        result: summation of number_1 and number_2 as integer

    Raises:
        IOError if integers are not given
    """
    if not (isinstance(number_1, int) and isinstance(number_2, int)):
        raise IOError(f"{number_1} and {number_2} must be integer.")
    return number_1 + number_2


if __name__ == '__main__':
    NUMBER_1 = '10'
    NUMBER_2 = 20

    result = add(NUMBER_1, NUMBER_2)
    print(f"Addition of {NUMBER_1} and {NUMBER_2} is: {result}")
