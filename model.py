import joblib
import pandas as pd

class Student:
    def __init__(self, name, weekly_study_hours, attendance, participation):
        self.name = name
        self.weekly_study_hours = weekly_study_hours
        self.__attendance = attendance
        self.__participation = participation

    def get_attendance(self):
        return self.__attendance

    def get_participation(self):
        return self.__participation

class StudentClassifier:
    def __init__(
        self,
        student,
        model_path="models/logistic_model.pkl",
        encoder_path="models/label_encoder.pkl"
    ):
        self.student = student
        self.model = joblib.load(model_path)
        self.encoder = joblib.load(encoder_path)

    def predict(self):
        data = pd.DataFrame([{
        "weekly_study_hours": self.student.weekly_study_hours,
        "attendance": self.student.get_attendance(),
        "participation": self.student.get_participation()
    }])
        prediction = self.model.predict(data)[0]
        result = self.encoder.inverse_transform([prediction])[0]
        return result