"""
This module shows how to implement a callable object.
Callable objects are convenient when we want to create
object and want to maintain the states across different
calls.

e.g. In keras deep learning library, we can get state
by createing layers in the below way-

tf.keras.layers.Conv2D(arguments)

To make an object callable we need to implement the
__call__() magic method.
"""

from collections import defaultdict

class CallCount:
    """
    This class implements a callable object.
    """
    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]


if __name__ == '__main__':
    CC = CallCount()
    ARG = 1 # should print 1 since calling first time with arg 1
    print(CC(ARG))
    ARG = 2 # should print 1 since calling first time with arg 2
    print(CC(ARG))
    ARG = 1 # should print 2 since calling second time with arg 1
    print(CC(1))
