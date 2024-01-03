"""Test cases for 7-Eleven."""

#Standard library

#3rd party library
import pytest

#project library
#from seven_eleven.secen from print_7_eleven
@pytest.mark.parametrize(
    "number, expected"
    [
        (1, 1),
        (2, 3),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, "seven"),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, "eleven"),
        (14, "seven"),
        (21, "seven"),
        (21, "seven")
    ]
)

def test_7_eleven(number, expected):
    """print 7-eleven"""
    #Arrang
    #Act
    #Assert
    