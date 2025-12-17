# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email


# 2. Combine the First and Last name into this format:
    #    "Last, First"  

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken

import student_data
students = student_data.students

id = input("What is your CPS Id numbers?")
for student in students:
    if id == student['CPSID']:
        print(student['CPSID'] )
        print("this works")

first_name = input("What is your name")
for student in students:
    if id == student['FName']:
        print(student['FName'])
        print("this works")

last_name = input("What is your last name?")
for student in students:
    if last_name == students:
        print(student['LName'])
        print("this works")

middle_name = input("What is your middle name?")
for student in students:
    if middle_name == students:
        print(student['MName'])
        print("this works")

Hr_second = int(input("What is your Homeroom?"))
for student in students:
    if Hr_second == students:
        print(student['HR'])
        print("this works")

Gl_second = int(input("What is your Grade Level?"))
for student in students:
    if Gl_second == students:
        print(student['GL'])
        print("this works")

Email_second = input("What is your Email?")
for student in students:
    if Email_second == students:
        print(student['Email'])
        print("this works")