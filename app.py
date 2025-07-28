import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("Farm_Irrigation_System.pkl")

# App layout
st.set_page_config(page_title="Smart Sprinkler System", layout="wide")
st.title("🌿 Smart Sprinkler System")
st.caption("Monitor your farm's irrigation with smart sensors")
st.markdown("Enter *scaled sensor values* between 0.0 and 1.0 to predict sprinkler ON/OFF status.")

# Divide sensors into 4 columns for better layout
sensor_values = []
cols = st.columns(4)
for i in range(20):
    with cols[i % 4]:
        val = st.slider(f"Sensor {i+1}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        sensor_values.append(val)

# Custom button styling
predict_btn = st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #34A853;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 8px;
    }
    div.stButton > button:first-child:hover {
        background-color: #2c8c45;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Prediction
if st.button("🔍 Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("###  Sprinkler Prediction")
    with st.container():
        for i, status in enumerate(prediction):
            color = "green" if status == 1 else "red"
            label = "🟢 ON" if status == 1 else "🔴 OFF"
            st.markdown(f"<span style='color:{color}; font-size:18px;'>Sprinkler {i+1} (Parcel {i+1}): {label}</span>", unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; font-size: 16px; color: gray; margin-top: 2rem;'>
        This application is developed as part of the<br>
        <strong>Shell-Edunet Skills4Future AICTE Internship Program</strong><br>
        under the project titled <strong>Smart Irrigation</strong>.
    </div>
    """,
    unsafe_allow_html=True
)


