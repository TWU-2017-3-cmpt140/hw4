CMPT 140 (Fall 2017) assignment #4

Data analysis on course registration system data

histHelper.py - function to help generate histogram

data/ - folder with some data files

data/fake_twu_student_info.csv - contains student number, name and birthdate of the students

data/course_schedules.csv - indicate schedule of courses

data/class_registrations.csv - indicates the courses the students registered. The first column indicates the student number and the second column indicates the course that the student is registered in.  There are multiple rows with the same student number since a student can be registered in more than one course.

sdb/ - folder for package sdb

sdb/__init__.py - package initialization script

The following are class definition files for classes in the sdb package

sdb/Course.py

sdb/Event.py

sdb/Schedule.py

sdb/Student.py

sdb/WeekDay.py
