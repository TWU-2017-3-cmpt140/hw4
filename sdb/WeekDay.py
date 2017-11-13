#*******************************************************************************
# CMPT 140 Assignment #3
# Enum for week days
# reference: https://docs.python.org/3/library/enum.html
#*******************************************************************************
from enum import Enum
class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5

    #***************************************************************************
    # less than operator
    # returns True if self < other, False otherwise
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.value < other.value
        else:
            NotImplemented

    #***************************************************************************
    # less than or equal operator
    # returns True if self <= other, False otherwise
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.value <= other.value
        else:
            NotImplemented

    #***************************************************************************
    # greater than operator
    # returns True if self > other, False otherwise
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.value > other.value
        else:
            NotImplemented

    #***************************************************************************
    # greater than or equal operator
    # returns True if self >= other, False otherwise
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.value >= other.value
        else:
            NotImplemented
