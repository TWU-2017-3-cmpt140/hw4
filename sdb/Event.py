#*******************************************************************************
# CMPT 140 Assignment #3
# Class Event definition file
#*******************************************************************************
class Event:
    """
    fields:
        day - WeekDay
        startTime - float 0-23 e.g. 8.5 to indicate 8:30
        endTime - float 0-23
    """

    #***************************************************************************
    # Class initializer
    # this function creates a WeeklyAppt object
    #
    # input: day, startTime, endTime
    def __init__(self, day, startTime, endTime):
        self.day = day
        self.startTime = startTime
        self.endTime = endTime

    #***************************************************************************
    # less than operator
    # returns True if self < other, False otherwise
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            byDay = self.day < other.day
            if byDay:
                return byDay
            else:
                return self.startTime < other.startTime
        else:
            NotImplemented

    #***************************************************************************
    # less than or equal operator
    # returns True if self <= other, False otherwise
    def __le__(self, other):
        if isinstance(other, self.__class__):
            byDay = self.day <= other.day
            if byDay:
                return byDay
            else:
                return self.startTime <= other.startTime
        else:
            NotImplemented

    #***************************************************************************
    # greater than operator
    # returns True if self > other, False otherwise
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            byDay = self.day > other.day
            if byDay:
                return byDay
            else:
                return self.startTime > other.startTime
        else:
            NotImplemented

    #***************************************************************************
    # greater than or equal operator
    # returns True if self >= other, False otherwise
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            byDay = self.day >= other.day
            if byDay:
                return byDay
            else:
                return self.startTime >= other.startTime
        else:
            NotImplemented

    #***************************************************************************
    # define criteria for equality
    #
    # input: object to compare
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.day == other.day and \
                self.startTime == other.startTime and \
                self.endTime == other.endTime
        return NotImplemented # indicate that you cannot compare Student
                              # object with instance of other classes


    #***************************************************************************
    # hash function; required for set operation
    #
    # return: an integer
    def __hash__(self):
        return self.day.value

    #***************************************************************************
    # return a string representation of this object
    #
    # return: a string
    def __str__(self):
        return str(self.day).split(".")[1] + ": " + \
            str(self.startTime) + \
            " to " + \
            str(self.endTime)
