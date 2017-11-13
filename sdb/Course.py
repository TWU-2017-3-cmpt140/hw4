#*******************************************************************************
# CMPT 140 Assignment #3
# Class Course definition file
#*******************************************************************************
class Course:
    """
    fields:
        name
        schedule
    """

    #***************************************************************************
    # Class initializer
    # this function creates a Course object
    #
    # input: name, schedule
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    #***************************************************************************
    # define criteria for equality
    #
    # input: object to compare
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            # notice we only require course with same name as equality
            # this means, course object with same name but DIFFERENT
            # schedule would be considered the SAME.  This will prevent
            # a student from registering the same course more than once
            return self.name == other.name
        return NotImplemented # indicate that you cannot compare Course
                              # object with instance of other classes

    #***************************************************************************
    # hash function; required for set operation
    #
    # return: an integer
    def __hash__(self):
        return hash(self.name) # generate an integer based on the course name

    #***************************************************************************
    # return a string representation of this object
    #
    # return: a string
    def __str__(self):
        return self.name + ": " + str(self.schedule)
