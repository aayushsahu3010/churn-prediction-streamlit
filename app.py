import streamlit as st
import joblib
import numpy as np


# ---------------------- Page configuration ----------------------
st.set_page_config(
    page_title="Churn Prediction App",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------------------- Sidebar ----------------------
st.sidebar.header("Customer Information")
age = st.sidebar.slider("Age", 10, 100, 30)
tenure = st.sidebar.slider("Tenure (Months)", 0, 130, 10)
monthlycharge = st.sidebar.number_input("Monthly Charge", min_value=30, max_value=150, value=50)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

# ---------------------- Load scaler and model ----------------------
if age>80 or monthlycharge>100 or tenure==0:
    model=joblib.load("model/bestModel.pkl")  
else:
  model = joblib.load("model/best_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# ---------------------- Main Title ----------------------
st.markdown(
    "<h1 style='text-align: center; color: #4B0082;'>📊 Churn Prediction App</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Predict whether a customer is likely to churn</p>", 
    unsafe_allow_html=True
)
st.divider()

# ---------------------- Predict Button ----------------------
if st.button("Predict"):
    # Encode gender
    gender_encoded = 1 if gender == "Male" else 0

    # Prepare input
    input_data = np.array([[age, tenure, monthlycharge, gender_encoded]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)[0]

    # Display results with styling
    if prediction == 1:
        st.markdown(
            "<h2 style='text-align: center; color: green;'> ✅The customer is likely to churn!</h2>", 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h2 style='text-align: center; color: red;'> ⚠️The customer is not likely to churn.</h2>", 
            unsafe_allow_html=True
        )
else:
    st.info("Please enter customer details in the sidebar and click 'Predict' to see the result.")

# ---------------------- Footer ----------------------
st.divider()
st.markdown(
    "<p style='text-align: center; color: gray;'>Developed by Komendra Sahu and Aayush sahu| 2025 (M-tech: DSAI) </p>",
    unsafe_allow_html=True
)




# ..........................WORKING FILE WITHOUT UI.................................

# import streamlit as st
# import joblib
# import numpy as np
# import streamlit as st
# import joblib
# import numpy as np

# # Load the scaler and model
# scaler = joblib.load("scaler.pkl")
# model = joblib.load("best_model.pkl")

# # App title
# st.title("Churn Prediction App")

# st.divider()
# st.write("Please enter the values and hit the predict button for getting a prediction.")
# st.divider()

# # Input fields
# age = st.number_input("Enter age", min_value=10, max_value=100, value=30)
# tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)
# monthlycharge = st.number_input("Enter Monthly Charge", min_value=30, max_value=150)
# gender = st.selectbox("Enter the Gender", ["Male", "Female"])

# st.divider()

# # Prediction button
# predictbutton = st.button("Predict!")

# if predictbutton:
#     # Encode gender
#     gender_encoded = 1 if gender == "Male" else 0

#     # Prepare input data
#     input_data = np.array([[age, tenure, monthlycharge, gender_encoded]])

#     # Scale input
#     input_scaled = scaler.transform(input_data)

#     # Make prediction
#     prediction = model.predict(input_scaled)[0]

#     # Show result
#     if prediction == 1:
#         st.success("The customer is likely to churn.")
#     else:
#         st.success("The customer is not likely to churn.")
# else:
#     st.write('please enter the values and use predict button')