"""
This module shows how context manager works
and how to define legacy context manager

Assumption: user needs to take backup of a
database and before taking backup, the database
needs to be stopped and after backup is finished
the databse needs to be started.

This modules show example of using a good
context manager using this use case.
"""

def stop_database():
    """A function that stops the database.

    This function stops an running databse
    without breaking any current operation.
    """
    print("stopping database.")

def start_databse():
    """A function to start a database.

    This function starts a stopped databse
    """
    print("starting databse.")

def backup_databse():
    """A function to taking backup of a databse.

    This function checks the database consistency
    and takes backup if no inconsistency found.
    """
    print("taking backup..")

class DBHandler:
    """A class tha defines a context manager

    This class acts as a context manager.
    The operation defines in __enter__
    method will be executed first, then
    the context work and then the operation
    defined in the __exit__ method will be
    executed.
    """
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        start_databse()


if __name__ == '__main__':
    with DBHandler(): # op seq stop db,backup,start db.
        backup_databse()
