#*******************************************************************************
# CMPT 140 Assignment #3
# Class Schedule definition file
#*******************************************************************************
class Schedule:
    """
    fields:
        events - set of Event objects
    """

    #***************************************************************************
    # Class initializer
    # this function creates a Schedule object
    #
    # input: name, schedule
    def __init__(self):
        self.events = set() # weekly class events

    #***************************************************************************
    # define criteria for equality
    #
    # input: object to compare
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.events == other.events
        return NotImplemented # indicate that you cannot compare Student
                              # object with instance of other classes

    #***************************************************************************
    # return a string representation of this object
    #
    # return: a string
    def __str__(self):
        out = ""
        if len(self.events)==0:
            return ""
        li = list(self.events)
        li.sort()
        for evt in li[:-1]:
            out = out + str(evt) + ", "
        out = out + str(li[-1])
        return out
