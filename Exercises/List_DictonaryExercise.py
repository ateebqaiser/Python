# Task 2: Student Info Collector
# Topic Covered: list, dictionary, input(), for loop
# Task:
# Ask the user to enter 3 students' names and their grades.
# Store this in a dictionary with names as keys and grades as values.
# Then print the full dictionary.

studentdata = {
    "s_name" : [],
    "s_grade" : []
}
# studentdata = {}

print("Welcome to Student Info Collector\nEnter 3 student names with thier grades")
for i in range(1,4):
    name=input(f"Enter {i} student name = ")
    grade=input("Enter thier grade = ")[0]

    studentdata["s_name"].append(name)
    studentdata["s_grade"].append(grade)
    # studentdata[name]=grade

for j in range(0,3):
    print(f"Student name = {studentdata["s_name"][j]} and thier Grade = {studentdata["s_grade"][j]}")

#print(studentdata)
# print(f"Student names {studentdata["s_name"]}")
# print(f"Student grades {studentdata["s_grade"]}")
