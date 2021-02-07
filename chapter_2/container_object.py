"""
This module shows how to implement a container object so
that the operation like bellow can be performed:

element in container - will return true or false

for this purpose, the object should have a method like

container.__contains__(element)

E.g. lets assume we have a grid of geomap, we want to
check if a specific coordinate is in that grid or not.
"""

class Bounderies:
    """
    This class implements the internal op
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __contains__(self, coord):
        x_w, y_h = coord
        return 0 <= x_w < self.width and 0 <= y_h < self.height

class Grid:
    """
    This class implements the grid or the geomap
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.limits = Bounderies(self.height, self.width)

    def __contains__(self, coord):
        return coord in self.limits


if __name__ == '__main__':
    HEIGHT = 200
    WIDTH = 300
    grid = Grid(HEIGHT, WIDTH)
    COORD = (300, 60)   # should be false
    print(COORD in grid)
    COORD = (40, 80)    # should be true
    print(COORD in grid)
