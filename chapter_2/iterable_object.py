"""
This module  shows how to design an iterable
object, so that it can be iterated over using
a for loop that gets one item at a time.
"""

from datetime import timedelta, date

class DateRangeIterable:
    """This class represent an iterable object
    """
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    @property
    def next(self):
        """A method to defin property to get
        next day without accessing __next__()
        magic method explicitly.
        """
        return self.__next__()

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration()
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


if __name__ == '__main__':
    START_DATE = date(2018, 1, 1)
    END_DATE = date(2018, 1, 5)
    for day in DateRangeIterable(START_DATE, END_DATE):
        print(day)

    # we also can define next property to easily get next day
    # without accessing the __next__ magic method explicitly
    it = DateRangeIterable(START_DATE, END_DATE)
    print(it.next)
    print(it.next)
