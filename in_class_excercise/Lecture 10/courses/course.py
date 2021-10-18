'''
Sample Code
CS 5001, Fall 2020 - Lecture 10

A class representing a Course.
'''
from queue_impl import Queue


class Course:
    '''
        Class -- Course
            A course.
        Attributes:
            course_num -- The course number.
            capacity -- The number of places in the course.
            roster -- A set of registered students.
            waitlist -- A Queue of students waiting to get in to the course.
        Methods:
            register_student -- Adds a student to the roster if there is space.
            Otherwise, adds them to the waitlist.
            drop_student -- Drops a student from the course. Automatically
            registers the first student from the waitlist in their place, if
            applicable.
    '''
    def __init__(self, course_num, capacity):
        '''
            Constructor -- creates a new instance of Course.
            Parameters:
                self -- the current Course object.
                course_num -- The course number.
                capacity -- The number of places in the course.
        '''
        self.course_num = course_num
        self.capacity = capacity
        self.roster = set()
        self.waitlist = Queue()

    
    def register_student(self, student):
        '''
            Method -- register_student
                Adds a student to the roster if there is space. Otherwise, adds
                them to the waitlist.
            Parameters:
                self -- The current Course object.
                student -- The Student to register.
        '''
        if len(self.roster) < self.capacity:
            self.roster.add(student)
            student.add_course(self)
        else:
            self.waitlist.enqueue(student)
            student.wait_for_course(self)

    def drop_student(self, student):
        '''
            Method -- drop_student
                Drops a student from the course. Automatically registeres the
                first student from the waitlist.
            Parameters:
                self -- The current Course object.
                student -- The Student to drop.
        '''
        if student in self.roster:
            self.roster.remove(student)
            student.remove_course(self)
            if self.waitlist.is_empty() == False:
                next_student = self.waitlist.dequeue()
                self.roster.add(next_student)
                next_student.add_course(self)
                next_student.stop_waiting(self)