'''
Sample Code
CS 5001, Fall 2020 - Lecture 10

A class representing a registration database. Contains a set of Course objects.
'''


class RegistrationDB:
    '''
        Class -- RegistrationDB
            A registration database.
        Attributes:
            courses -- A set of Course objects.
        Methods:
            get_course -- Gets a Course by course number.
            add_student_to_course -- Registers a student for a course.
            drop_student_from_course -- Drops a student from a course.
    '''
    def __init__(self, courses):
        '''
            Constructor -- creates a new instance of RegistrationDB.
            Parameters:
                self -- the current RegistrationDB object.
                courses -- a set of Courses
        '''
        self.courses = courses

    def get_course(self, course_num):
        '''
            Method -- get_course
                Gets the Course object with the given course number. Assumes
                the Course exists.
            Parameters:
                self -- the current RegistrationDB
                course_num -- the course number, an integer
            Returns:
                The Course object.
        '''
        for course in self.courses:
            if course.course_num == course_num:
                return course


    def add_student_to_course(self, student, course_num):
        '''
            Method -- add_student_to_course
                Registers a student for a course.
            Parameters:
                self -- the current RegistrationDB
                student -- the Student to register
                course_num -- the course number, an integer
            Returns:
                The Course object.
        '''
        course = self.get_course(course_num)
        course.register_student(student)

    def drop_student_from_course(self, student, course_num):
        '''
            Method -- drop_student_from_course
                Drops a student from a course.
            Parameters:
                self -- the current RegistrationDB
                student -- the Student to drop
                course_num -- the course number, an integer
            Returns:
                The Course object.
        '''
        course = self.get_course(course_num)
        course.drop_student(student)