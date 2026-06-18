# 🎓 Student Result Prediction System (Machine Learning Project)

## 📌 Project Overview
This project is a simple Machine Learning system that predicts whether a student will **PASS or FAIL** based on academic and behavioral features.

The model is trained using **Logistic Regression** and takes into account:
- Weekly Study Hours
- Attendance Percentage
- Class Participation

---

## 🧠 Problem Statement
To build a predictive model that can estimate student performance using basic academic engagement features.

This helps in understanding how study habits and attendance impact student outcomes.

---

## ⚙️ Features Used
The model uses the following input features:

- 📚 Weekly Study Hours (continuous value)
- 🏫 Attendance Percentage 
- 🎯 Class Participation 

---

## 🤖 Machine Learning Model
- Algorithm: Logistic Regression
- Type: Supervised Learning
- Task: Binary Classification (PASS / FAIL)
- Library: Scikit-learn

---

## 📊 Dataset Information
- Total Records: ~100 rows
- Type: Synthetic dataset (created for learning purposes)
- Format: CSV file

### Columns:
- name
- weekly_study_hours
- attendance
- participation
- result (PASS / FAIL)

---

## 🎯 Model Performance
- Accuracy: ~90%
- Evaluation Method: Train-Test Split

---

## 🚀 How to Run This Project

### 1. Install Required Libraries
```bash
pip install pandas scikit-learn joblib
