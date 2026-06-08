import streamlit as st
import pandas as pd
import pickle

# Load Model
with open("TeenDepressionAnalysisModel.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Teen Depression Prediction")

# Input Fields
age = st.number_input("Age", min_value=13, max_value=19, value=16)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

daily_social_media_hours = st.slider(
    "Daily Social Media Hours",
    0.0, 15.0, 5.0
)

platform_usage = st.selectbox(
    "Platform Usage",
    ["Instagram", "TikTok", "Both"]
)

sleep_hours = st.slider(
    "Sleep Hours",
    0.0, 12.0, 7.0
)

screen_time_before_sleep = st.slider(
    "Screen Time Before Sleep (Hours)",
    0.0, 5.0, 1.0
)

academic_performance = st.slider(
    "Academic Performance",
    1, 10, 5
)

physical_activity = st.slider(
    "Physical Activity Level",
    1, 10, 5
)

social_interaction_level = st.slider(
    "Social Interaction Level",
    1, 10, 5
)

stress_level = st.slider(
    "Stress Level",
    1, 10, 5
)

anxiety_level = st.slider(
    "Anxiety Level",
    1, 10, 5
)

addiction_level = st.slider(
    "Addiction Level",
    1, 10, 5
)

# Simple Encoding
gender = 1 if gender == "Male" else 0

platform_dict = {
    "Instagram": 0,
    "TikTok": 1,
    "Both": 2
}

platform_usage = platform_dict[platform_usage]

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "daily_social_media_hours": [daily_social_media_hours],
        "platform_usage": [platform_usage],
        "sleep_hours": [sleep_hours],
        "screen_time_before_sleep": [screen_time_before_sleep],
        "academic_performance": [academic_performance],
        "physical_activity": [physical_activity],
        "social_interaction_level": [social_interaction_level],
        "stress_level": [stress_level],
        "anxiety_level": [anxiety_level],
        "addiction_level": [addiction_level]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error(" High Risk of Depression")
    else:
        st.success("Low Risk of Depression")