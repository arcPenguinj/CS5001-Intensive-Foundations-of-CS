'''
Sample Code
CS 5001, Fall 2020 - Lecture 10

A class representing a Student.
'''


class Student:
    '''
        Class -- Student
            A student.
        Attributes:
            student_id -- The student's ID number
            courses -- The courses the student is registered for
            wait_courses - The courses the student is waitlisted for
        Methods:
            add_course -- Add a course to the student's schedule.
            wait_for_course -- Adds a course to the student's waitlist.
            remove_course -- Removes a course form the student's schedule.
            stop_waiting -- Removes a course from the student's waitlist.
    '''
    def __init__(self, student_id):
        '''
            Constructor -- creates a new instance of Student.
            Parameters:
                self -- The current Student object.
                student_id -- The student's ID number.
        '''
        self.id = student_id
        self.courses = set()
        self.wait_courses = set()

    def add_course(self, course):
        '''
            Method -- add_course
                Adds a course to the student's schedule.
            Parameters:
                self -- The current Student.
                course -- The course to add.
        '''
        self.courses.add(course)

    def wait_for_course(self, course):
        '''
            Method -- wait_for_course
                Adds a course to the student's waitlist.
            Parameters:
                self -- The current Student.
                course -- The course to add.
        '''
        self.wait_courses.add(course)


    def remove_course(self, course):
        '''
            Method -- remove_course
                Removes a course from the student's schedule.
            Parameters:
                self -- The current Student.
                course -- The course to remove.
        '''
        self.courses.remove(course)

    def stop_waiting(self, course):
        '''
            Method -- stop_waiting
                Removes a course from the student's waitlist.
            Parameters:
                self -- The current Student.
                course -- The course to remove.
        '''
        self.wait_courses.remove(course)