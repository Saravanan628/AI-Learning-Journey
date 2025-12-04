import json

students = []

n = int(input("How many students do you want to add? "))

for i in range(n):
    print(f"\nEnter details of student {i + 1}:")
    student = {}
    student["name"] = input("Enter student name: ")
    student["rollno"] = input("Enter roll number: ")
    student["department"] = input("Enter department: ")
    student["marks"] = int(input("Enter marks: "))

    students.append(student)

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)


