"""
This module shows how to use properties
to confirm that one method is doing one
thing at a time
"""

class Coordinates:
    """A class to define coordinates of a place
    """
    def __init__(self, lat: float, long: float) -> None:
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        """A method to return the latitude as property
        """
        return self._latitude

    @latitude.setter
    def latitude(self, lat_val: float) -> None:
        if lat_val not in range(-90, 90 + 1):
            raise ValueError(f"{lat_val} not a valid latitude value.")
        self._latitude = lat_val

    @property
    def longitude(self) -> float:
        """A method to return the longitude as property
        """
        return self._longitude

    @longitude.setter
    def longitude(self, long_val: float) -> None:
        if long_val not in range(-180, 180 + 1):
            raise ValueError(f"{long_val} not a valid longiture value.")
        self._longitude = long_val


if __name__ == '__main__':
    cord = Coordinates(20, 30)
    cord.latitude = 50
    cord.longitude = 180
    print(cord.latitude)
    print(cord.longitude)
