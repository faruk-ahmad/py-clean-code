"""
This module shows the use of contextlib
for defining context manager.
"""

import contextlib

def stop_database():
    """A function to stops a database
    """
    print("stoping the database")

def start_database():
    """A function to start a databsae
    """
    print("starting the database")

def backup_database():
    """A function to backup a database
    """
    print("backup the database")

@contextlib.contextmanager
def db_handler():
    """A function that acts like a context manager
    """
    try:
        stop_database()
        yield
    finally:
        start_database()


if __name__ == "__main__":
    with db_handler():
        backup_database()
        