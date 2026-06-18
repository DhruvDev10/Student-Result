from model import Student, StudentClassifier

def main():
    print("\n===== STUDENT RESULT PREDICTION =====")
    name = input("Enter Name: ").strip()

    try:
        study_hours = float(input("Enter Weekly Study Hours: "))
        attendance = float(input("Enter Attendance (%): "))
        participation = float(input("Enter Class Participation (0-10): "))
    except ValueError:
        print("ERROR: Please enter numeric values only.")
        return

    if study_hours < 0:
        print("ERROR: Study hours cannot be negative.")
        return

    if not (0 <= attendance <= 100):
        print("ERROR: Attendance must be between 0 and 100.")
        return

    if not (0 <= participation <= 10):
        print("ERROR: Participation must be between 0 and 10.")
        return

    student = Student(
        name,
        study_hours,
        attendance,
        participation
    )

    classifier = StudentClassifier(student)
    result = classifier.predict()

    print("\n========== RESULT ==========")
    print(f"Name: {name}")
    print(f"Predicted Result: {result}")
    print("============================")

if __name__ == "__main__":
    main()