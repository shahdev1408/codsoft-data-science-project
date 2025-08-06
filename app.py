# import streamlit as st
# import numpy as np
# import joblib
# from PIL import Image

# # Load custom CSS
# with open("style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Load trained model
# # Load the model
# model = joblib.load('titanic_model.pkl')

# # Set page config with custom icon
# st.set_page_config(page_title="Titanic Survival Prediction", page_icon="🚢", layout="centered")

# # Optional: Load and display a banner image (logo or header)
# st.image("./logo.png", use_container_width=True)

# # Title & Description
# st.title("🧠 AI-Powered Titanic Survival Predictor")
# st.markdown("Predict the survival chances of Titanic passengers using a machine learning model.")

# st.markdown("---")

# # 🎯 Example Passenger Selector
# sample_passengers = {
#     "Young 1st Class Woman": [1, 0, 25, 0, 0, 100, 1],
#     "Old 3rd Class Man": [3, 1, 60, 0, 0, 7.25, 0],
#     "Child with Family": [2, 0, 8, 1, 2, 35, 2]
# }

# selected_sample = st.selectbox("🎯 Try a Sample Passenger (optional)", ["None"] + list(sample_passengers.keys()))

# # Default values
# if selected_sample != "None":
#     values = sample_passengers[selected_sample]
#     pclass, sex, age, sibsp, parch, fare, embarked = values
# else:
#     # Manual Input
#     pclass = st.selectbox("Passenger Class", options=[1, 2, 3])
#     sex = st.radio("Sex", options=["male", "female"])
#     age = st.slider("Age", 1, 100, 25)
#     sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", 0, 10, 0)
#     parch = st.number_input("Parents/Children Aboard (Parch)", 0, 10, 0)
#     fare = st.number_input("Fare Paid", 0.0, 600.0, 32.0)
#     embarked = st.selectbox("Port of Embarkation", options=["S", "C", "Q"])

#     # Encode inputs
#     sex = 1 if sex == "male" else 0
#     embarked = {"S": 0, "C": 1, "Q": 2}[embarked]

# # Final prediction input
# features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])

# # Predict button
# if st.button("🚀 Predict Survival"):
#     prediction = model.predict(features)[0]
#     if prediction == 1:
#         st.success("🎉 The passenger would have **SURVIVED**!")
#     else:
#         st.error("💀 The passenger would have **NOT SURVIVED**.")

# st.markdown("---")

# # 📢 Footer
# st.markdown("""
# <div style='text-align: center; font-size: 14px; color: gray;'>
# Built with ❤️ using <b>Python</b>, <b>Streamlit</b> and <b>scikit-learn</b><br>
# <a href='https://github.com/yourgithub'>View on GitHub</a>
# </div>
# """, unsafe_allow_html=True)




import streamlit as st
import numpy as np
import joblib
from PIL import Image, ImageDraw, ImageFont
import os

# Page config
st.set_page_config(page_title="Titanic Survival Prediction", page_icon="🚢", layout="centered")

# Custom CSS
with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load model
model = joblib.load("titanic_model.pkl")

# Load base image
base_image = Image.open("base.png")  # This is the image with robot

# Page Header
st.image("logo.png", use_container_width=True)
st.title("🧠 AI-Powered Titanic Survival Predictor")
st.markdown("Predict the survival chances of Titanic passengers using a machine learning model.")
st.markdown("---")

# Sample passengers
sample_passengers = {
    "Young 1st Class Woman": [1, 0, 25, 0, 0, 100, 1],
    "Old 3rd Class Man": [3, 1, 60, 0, 0, 7.25, 0],
    "Child with Family": [2, 0, 8, 1, 2, 35, 2]
}

selected_sample = st.selectbox("🎯 Try a Sample Passenger (optional)", ["None"] + list(sample_passengers.keys()))

# Default or manual input
if selected_sample != "None":
    pclass, sex, age, sibsp, parch, fare, embarked = sample_passengers[selected_sample]
else:
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.radio("Sex", ["male", "female"])
    age = st.slider("Age", 1, 100, 25)
    sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", 0, 10, 0)
    parch = st.number_input("Parents/Children Aboard (Parch)", 0, 10, 0)
    fare = st.number_input("Fare Paid", 0.0, 600.0, 32.0)
    embarked = st.selectbox("Port of Embarkation", ["S", "C", "Q"])

    sex = 1 if sex == "male" else 0
    embarked = {"S": 0, "C": 1, "Q": 2}[embarked]

features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])

# Predict button
if st.button("🚀 Predict Survival"):
    prediction = model.predict(features)[0]
    result_text = "SURVIVED" if prediction == 1 else "NOT SURVIVED"
    result_color = (0, 255, 0) if prediction == 1 else (255, 0, 0)

    # Modify image with result
    img = base_image.copy()
    draw = ImageDraw.Draw(img)

    # Load custom font (optional: use system font if available)
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    # Position (adjust as needed to match the robot head in your image)
    x, y = 850, 300
    draw.text((x, y), result_text, fill=result_color, font=font)

    st.image(img, caption=f"Prediction: {result_text}", use_container_width=True)
else:
    st.image(base_image, use_container_width=True)

st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 14px; color: gray;'>
Built with ❤️ using <b>Python</b>, <b>Streamlit</b> and <b>scikit-learn</b><br>
            created by <b>Shah Dev</b><br>
<a href='https://github.com/shahdev1408'>View on GitHub</a>
</div>
""", unsafe_allow_html=True)
