# 🚢 Titanic Survival Prediction

A high-tech Streamlit dashboard that predicts whether a passenger would survive the Titanic disaster using machine learning. This project includes a realistic UI and predictive logic based on passenger details such as age, gender, class, and more.

![Demo Screenshot](screenshot.png) <!-- Optional: Add an actual screenshot image in your repo -->

---

## 📌 Project Objective

The goal is to build a machine learning model that predicts survival on the Titanic, and wrap it in a **beautiful, futuristic dashboard** using **Streamlit** and **custom CSS styling**.

---

## 💡 Problem Statement

The Titanic dataset is a classic ML dataset that contains details of passengers. Based on features like:

- Passenger Class
- Age
- Sex
- Number of siblings/spouses aboard
- Number of parents/children aboard
- Fare

...we predict whether a passenger **survived (1)** or **not (0)**.

---

## 📁 Project Structure

titanic-prediction/
├── app.py # Main Streamlit app
├── titanic_model.pkl # Trained ML model file
├── style.css # Custom high-tech CSS
├── titanic.csv # Dataset (optional)
├── README.md # This file
├── logo.png
├── base.png
└── requirements.txt # Python dependencies
└── requirements.txt # Python dependencies


---

## 🚀 Features

- 🔍 Takes user input for passenger details
- 📊 Displays prediction result: **SURVIVED** or **NOT SURVIVED**
- 🤖 ML model trained using Logistic Regression
- 🎨 4K realistic dashboard with high-tech CSS styling
- 🧠 Live prediction using trained `.pkl` model
- 🧩 Custom image with dynamic label display

---

## 🛠️ How to Run the App

### Step 1: Clone the Repo

```bash
git clone https://github.com/shahdev1408/codsoft-data-science-project.git
cd codsoft-data-science-project/titanic-prediction


step 2

python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On Mac/Linux

step 3
pip install -r requirements.txt

step 4
streamlit run app.py



📷 UI Showcase
Clean futuristic UI with glowing neon buttons and shadows

CSS-powered hover effects and transitions

Dynamic prediction text over robot image

🧠 ML Model
Trained using LogisticRegression

Preprocessing: Label Encoding + Feature Selection

Model saved as titanic_model.pkl using joblib

📚 Dataset
Dataset: Kaggle Titanic Dataset

🙌 Acknowledgements
This project is part of the CodSoft Internship Projects.
Built with python,stremlit,scikitlearn
created by Shah Dev
