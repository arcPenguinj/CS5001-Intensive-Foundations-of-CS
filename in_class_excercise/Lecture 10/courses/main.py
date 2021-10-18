'''
Sample Code
CS 5001, Fall 2020 - Lecture 10

An example use case for the Queue data structure: managing the waitlist in a
course registration system.
'''
from course import Course
from registrationdb import RegistrationDB
from student import Student


def read_registrations(reg_file, db):
    '''
        Function -- read_registrations
            Reads in a file containing registration information and processes
            course registrations. TODO: Improve the design by breaking down
            this function.
        Parameters:
            reg_file -- the path to the registration file.
            db -- a RegistrationDB instance.
        Returns:
            A set containing all successfully registered students.
    '''
    students = set()
    try:
        with open(reg_file, "r") as file:
            curr_line = 0
            for line in file:
                if curr_line == 0:
                    # header row - don't process anything
                    curr_line += 1
                else:
                    parts = line.split(",") # break the line into table cells
                    student_id = parts[0].strip() # remove any whitespace
                    student = Student(student_id)
                    students.add(student)
                    for i in range(1, len(parts)):
                        course = int(parts[i].strip())
                        db.add_student_to_course(student, course)
    except FileNotFoundError:
        print("Registration file doesn't exist!")
    return students


# PURPOSE
# Reads in the file containing course drop information and processes the updates
# SIGNATURE
# read_drops :: String, RegistrationDB, Set<Student>
def read_drops(drop_file, db, students):
    '''
        Function -- read_drops
            Reads in a file containing course drop information and processes
            the updates. TODO: Improve the design by breaking down this
            function.
        Parameters:
            drop_file -- the path to the drop file.
            db -- a RegistrationDB instance.
    '''
    try:
        with open(drop_file, "r") as file:
            curr_line = 0
            for line in file:
                if curr_line == 0:
                    # header row - don't process anything
                    curr_line += 1
                else:
                    parts = line.split(",") # break the line into table cells
                    student_id = parts[0].strip() # remove any whitespace
                    student = get_student_by_id(student_id, students)
                    for i in range(1, len(parts)):
                        course = int(parts[i].strip())
                        db.drop_student_from_course(student, course)
    except FileNotFoundError:
        print("Drop file doesn't exist!")


def get_student_by_id(student_id, students):
    '''
        Function -- get_student_by_id
            Gets the student with the given id from a set of students.
        Parameters:
            student_id -- The student id to search for.
            students -- A set of Student objects to search in.
        Returns:
            A Student object, if found. Returns None if the student is not
            found.
    '''
    for student in students:
        if student.id == student_id:
            return student
    return None # If the student does not exist


def main():
    # keeping capacity low for easier testing
    cs5001 = Course(5001, 1)
    cs5002 = Course(5002, 1)
    cs5010 = Course(5010, 1)
    cs5800 = Course(5800, 1)
    cs5340 = Course(5340, 1)
    cs7180 = Course(7180, 1)
    cs6500 = Course(6500, 1)

    all_courses = {cs5001,cs5002,cs5010,cs5800,cs5340,cs7180,cs6500}
    
    db = RegistrationDB(all_courses)

    reg_file = "add_courses.txt"

    students = read_registrations(reg_file, db)

    for course in db.courses:
        print("Registrations for " + str(course.course_num))
        for student in course.roster:
            print(student.id)
        print(str(course.waitlist.size()) + " students waiting\n")

    drop_file = "drop_courses.txt"

    print("Processing drops...")

    read_drops(drop_file, db, students)

    for course in db.courses:
        print("Waiting students " + str(course.course_num))
        print(course.waitlist.size(), "\n")


if __name__ == "__main__":
    main()
