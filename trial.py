import csv
import os
from abc import ABC, abstractmethod

FILE_NAME = "students.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "name",
            "weekly_study_hours",
            "attendance",
            "participation",
            "marks",
            "result"
        ])

class MLModel(ABC):
    @abstractmethod
    def predict(self):
        pass

class Student:
    def __init__(self, name, weekly_study_hours,
                 attendance, participation):
        self.name = name
        self.weekly_study_hours = weekly_study_hours
        self.__attendance = attendance
        self.__participation = participation

    def get_attendance(self):
        return self.__attendance

    def get_participation(self):
        return self.__participation

class AdvancedPredictionModel(MLModel):
    def __init__(self, student):
        self.student = student

    def predict(self):
        hours = self.student.weekly_study_hours
        attendance = self.student.get_attendance()
        participation = self.student.get_participation()
        study_score = min(hours, 20) / 20 * 30
        attendance_score = attendance / 100 * 50
        participation_score = participation / 10 * 20

        marks = (
            study_score +
            attendance_score +
            participation_score
        )
        marks = min(marks, 100)

        if attendance < 50:
            result = "FAIL"
        elif marks >= 50:
            result = "PASS"
        else:
            result = "FAIL"
        return round(marks, 2), result

name = input("Enter Name: ").strip()
weekly_study_hours = float(input("Enter Weekly Study Hours: "))
attendance = float(input("Enter Attendance Percentage (0-100): "))
participation = float(input("Enter Class Participation (0-10): "))

if attendance < 0 or attendance > 100:
    print("ERROR: Attendance must be between 0 and 100.")
    exit()

if participation < 0 or participation > 10:
    print("ERROR: Participation must be between 0 and 10.")
    exit()

with open(FILE_NAME, "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if row and row[0].lower() == name.lower():
            print("\nERROR: Student already exists!")
            exit()

student = Student(
    name,
    weekly_study_hours,
    attendance,
    participation
)

model = AdvancedPredictionModel(student)
marks, result = model.predict()

with open(FILE_NAME, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        name,
        weekly_study_hours,
        attendance,
        participation,
        marks,
        result
    ])

print("\n========== RESULT ==========")
print(f"Name: {name}")
print(f"Weekly Study Hours: {weekly_study_hours}")
print(f"Attendance: {attendance}%")
print(f"Class Participation: {participation}/10")
print(f"Marks Obtained: {marks}%")
print(f"Final Result: {result}")
print("============================")