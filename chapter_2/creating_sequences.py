"""
This module shows how to implement
a sequence object so that items can
be accessed with index.
"""

from datetime import timedelta, date

class DateRangeSequence:
    """This class represent a date sequnce
    that can be accessed with index.
    """

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


if __name__ == '__main__':
    START_DATE = date(2018, 1, 1)
    END_DATE = date(2018, 1, 5)
    dt = DateRangeSequence(START_DATE, END_DATE)

    for d in dt:
        print(d)

    print(dt[0])
    print(dt[3])
