#*******************************************************************************
# CMPT 140 Assignment #3
# Class Student definition file
#*******************************************************************************
import datetime
from sdb.Event import *
class Student:
    """
    fields:
        studentNumber
        firstName
        lastName
        birthDate
        courses - set of Course objects
    """

    #***************************************************************************
    # Class initializer
    # this function creates a Student object
    #
    # input: studentNumber, firstName, lastName, birthDate
    def __init__(self, studentNumber, firstName, lastName, birthDate):
        self.studentNumber = studentNumber
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = datetime.datetime.strptime(birthDate,"%Y-%m-%d")
        self.courses = set() # let courses be a set

    #***************************************************************************
    # define criteria for equality
    #
    # input: object to compare
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.studentNumber == other.studentNumber
        return NotImplemented # indicate that you cannot compare Student
                              # object with instance of other classes


    #***************************************************************************
    # returns a string representation of this instance
    #
    # returns: a string
    def __str__(self):
        return self.lastName+", "+self.firstName+\
    " ("+str(self.studentNumber)+")"

    #***************************************************************************
    # getAge() calculate age of student
    #
    # returns an integer representing the age
    def getAge(self):
        now = datetime.datetime.now() # current date
        return int((now-self.birthDate).days/365)

    #***************************************************************************
    # add the specified course
    #
    # return True if courses added successfully, otherwise False
    def addCourse(self, course):
        if not (course in self.courses) and not self.conflictWith(course):
            self.courses.add(course)
            return True
        else:
            return False # student already registered for this course

    #***************************************************************************
    # remove the specified course
    #
    # return True if courses removed successfully, otherwise False
    def removeCourse(self, course):
        if course in self.courses:
            self.courses.remove(course)
            return True
        else:
            return False # student not registered for this course

    #***************************************************************************
    # check to see if the input course creates conflicts with any registered
    # courses
    #
    # can assume
    #     1. all courses will be between 8am-6pm.
    #     2. all classes starts either on the hour or 30 minutes afte the hour
    #        (e.g. 13:30, 14:30).
    #     3. all clases are either 1 hour long or 1.5 hours long.
    #
    # returns True if there is conflict, False otherwise
    # helper class to check for conflicts
    def conflictWith(self, course):
        # helper class:
        class CEvent(Event):
            def __init__(self, day, startTime, endTime):
                super().__init__(day, startTime, endTime)
            # overload equal - returns True if there is a conflicts
            # so this is not really "equal" in the sense the the two events
            # need to overlap each other completely
            def __eq__(self, other):
                if isinstance(other, self.__class__):
                    if (self.day != other.day):
                        return False # if date different, must NOT be equal
                    elif self.endTime <= other.startTime or \
                        other.endTime <= self.startTime:
                        return False # end before start, must not be equal
                    else:
                        return True # time overlap
                return NotImplemented # indicate that you cannot compare Student
                                      # object with instance of other classes
            # https://docs.python.org/3.6/reference/datamodel.html
            # If a class that overrides __eq__() needs to retain the
            # implementation of __hash__() from a parent class, the interpreter
            # must be told this explicitly by setting
            # __hash__ = <ParentClass>.__hash__.
            def __hash__(self):
                return super().__hash__()
        # get the list of ALL events
        allEvents = set()
        for c in self.courses:
            allEvents = allEvents.union(\
                [CEvent(e.day, e.startTime, e.endTime) \
                for e in c.schedule.events])
        return any([CEvent(e.day, e.startTime, e.endTime) in allEvents \
            for e in course.schedule.events])

    #***************************************************************************
    # list the courses the student is currently enrolled in
    #
    # returns a list of Course objects
    def listCourses(self):
        return list(self.courses)

    #***************************************************************************
    # print this student's time table to the console
    #
    # can assume all course names are 7 characters long e.g. CMPT140
    #
    # example output:
    #
    #       MONDAY   TUESDAY  WEDNESDAY  THURSDAY  FRIDAY
    # 08:00 CMPT140           CMPT140              CMT140
    # 08:30 CMPT140           CMPT140              CMT140
    # 09:00
    # 09:30
    # 10:00          BIOL103             BIOL103
    # 10:30          BIOL103             BIOL103
    # 11:00          BIOL103             BIOL103
    # 11:30
    # 12:00
    # 12:30
    # 13:00 MATH101           MATH101              MATH101
    # 13:30 MATH101           MATH101              MATH101
    # 14:00
    # 14:30
    # 15:00
    # 15:30
    # 16:00
    # 16:30
    # 17:00
    # 17:30
    # 18:00
    #
    # returns None
    def printTimeTable(self):
        # helper function to format time
        # e.g. 10 -> 10:00
        #      9.5 -> 09:30
        def formatTime(t):
            h = "0"+str(int(t//1)) if t<10 else str(int(t//1))
            m = "00" if t==t//1 else "30"
            return(h+":"+m)
        h = []
        for i in ["0"+str(h) if h<10 else str(h) for h in range(8,19)]:
            h = h + [i,i]
        m = ["00" if h%2==0 else "30" for h in range(0,21)]
        hm = [h+":"+m for h,m in zip(h,m)]
        eventDict = {}
        for c in self.courses:
            for e in c.schedule.events:
                d = str(e.day).split(".")[1]
                for t in [formatTime(x/10) \
                    for x in list(\
                        range(int(e.startTime*10),int(e.endTime*10),5))]:
                    eventDict[d,t] = c.name
        header = ["","MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
        colWidth = [6, 8, 9, 11, 10, 7]
        # print header
        headerLine = ""
        for i in range(0,len(header)):
            headerLine = headerLine + header[i] + " "*(colWidth[i]-len(header[i]))
        print(headerLine)
        for t in hm:
            line = ""
            for i,d in enumerate(header):
                if d=="":
                    line = line + t + " "*(colWidth[i] - len(t))
                else:
                    cName = eventDict.get((d,t),"")
                    line = line + cName + " "*(colWidth[i] - len(cName))
            print(line)
