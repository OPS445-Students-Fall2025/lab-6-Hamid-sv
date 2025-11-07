#!/usr/bin/env python3

# Author ID: ssamadivaghefi

# This script defines a Student class that stores name, number, and course grades.

# It includes methods to calculate GPA safely, display student info, 

# and list all courses the student passed (non-zero grades).

# Demonstrates basic class usage, exception handling, and dictionary iteration.

class Student:

    """Represent a student with a name, student number, and course grades."""



    # Define the name and number when a student object is created

    # Example: student1 = Student('john', 25969102)

    def __init__(self, name, number):

        # Always store both as strings so displayStudent() never breaks

        self.name = str(name)

        self.number = str(number)

        # Dictionary to store courses and grades: {'ops445': 3.5, ...}

        self.courses = {}



    # Return student name and number (no printing here)

    def displayStudent(self):

        return "Student Name: " + self.name + "\n" + "Student Number: " + self.number



    # Add or update a course grade for this student

    def addGrade(self, course, grade):

        # Store grade as float to be safe

        self.courses[course] = float(grade)



    # Calculate the GPA and return it in a formatted string

    def displayGPA(self):

        # If no courses, GPA is 0.0 (avoid ZeroDivisionError)

        if not self.courses:

            gpa = 0.0

        else:

            total = 0.0

            count = 0

            # Sum all grades and count how many

            for course in self.courses:

                total += self.courses[course]

                count += 1

            # Extra safety: if count somehow ends up 0, set GPA to 0.0

            if count == 0:

                gpa = 0.0

            else:

                gpa = total / count



        return "GPA of student " + self.name + " is " + str(gpa)

    # Return a list of courses where the student passed (grade not 0.0)

    def displayCourses(self):

        passed = []

        for course, grade in self.courses.items():

            if grade != 0.0:

                passed.append(course)

        return passed





if __name__ == '__main__':

    # Create first student object and add grades for each class

    student1 = Student('John', '013454900')

    student1.addGrade('uli101', 1.0)

    student1.addGrade('ops245', 2.0)

    student1.addGrade('ops445', 3.0)



    # Create second student object and add grades for each class

    student2 = Student('Jessica', '123456')

    student2.addGrade('ipc144', 4.0)

    student2.addGrade('cpp244', 3.5)

    student2.addGrade('cpp344', 0.0)



    # Display information for student1 object

    print(student1.displayStudent())

    print(student1.displayGPA())

    print(student1.displayCourses())



    # Display information for student2 object

    print(student2.displayStudent())

    print(student2.displayGPA())

    print(student2.displayCourses())
