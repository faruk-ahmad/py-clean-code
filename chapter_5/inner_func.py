"""
This module defines inner functions
"""

def parent():
    """This function shows how to define inner
    function.
    """
    print("Hello this from parent function.")

    def first_child():
        return "First Child"

    def second_child():
        return "Second Child"

    print(first_child() + " " + second_child())


if __name__ == '__main__':
    parent()
