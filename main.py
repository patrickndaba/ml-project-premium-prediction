import streamlit as st
import numpy as np
import random
import pickle
# -----------------------------
# Load your trained model (optional)
# -----------------------------
# Uncomment the following lines when you have a saved model file
# with open("health_insurance_model.pkl", "rb") as file:
#     model = pickle.load(file)

st.set_page_config(page_title="Health Insurance Cost Predictor", page_icon="💰", layout="centered")

st.title("💰 Health Insurance Cost Predictor")
st.write("Provide your details below to estimate your health insurance cost.")

# -----------------------------
# User Inputs
# -----------------------------

#age = st.number_input("Age", min_value=18, max_value=100, value=30)

#gender = st.selectbox("Gender", ['Male', 'Female'])

#region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])

#marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])

#bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])

#smoking_status = st.selectbox("Smoking Status", ['No Smoking', 'Regular', 'Occasional'])

#employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])

#income_level = st.selectbox("Income Level", ['<10L', '10L - 25L', '25L - 40L', '> 40L'])

#medical_history = st.selectbox("Medical History", [
    #'No Disease',
    #'Diabetes',
    #'High blood pressure',
    #'Diabetes & High blood pressure',
    #'Thyroid',
   # 'Heart disease',
    #'High blood pressure & Heart disease',
    #'Diabetes & Thyroid',
   # 'Diabetes & Heart disease'
#])

#insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])

# ------------------------------------------------------
# Layout: 4 rows (3 + 3 + 3 + 4 columns)
# ------------------------------------------------------

# Row 1
row1 = st.columns(3)
with row1[0]:
    age = st.number_input("Age", min_value=18, max_value=100, value=30,key='age_input')
with row1[1]:
    gender = st.selectbox("Gender", ['Male', 'Female'],key="gender_input")
with row1[2]:
    region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'],key="region_input")

# Row 2
row2 = st.columns(3)
with row2[0]:
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'],key="marital_status_input")
with row2[1]:
    bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'],key="bmi_category")
with row2[2]:
    smoking_status = st.selectbox("Smoking Status", ['No Smoking', 'Regular', 'Occasional'],key="smoking_status")

# Row 3
row3 = st.columns(3)
with row3[0]:
    employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'],key="employment_status")
with row3[1]:
    income_level = st.selectbox("Income Level", ['<10L', '10L - 25L', '25L - 40L', '> 40L'],key=" income_level ")
with row3[2]:
    insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'],key=" insurance_plan ")

# Row 4 (4 columns)
row4 = st.columns(4)
with row4[0]:
    medical_history = st.selectbox("Medical History", [
        'No Disease',
        'Diabetes',
        'High blood pressure',
        'Diabetes & High blood pressure',
        'Thyroid',
        'Heart disease',
        'High blood pressure & Heart disease',
        'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],key="medical_history")
with row4[1]:
    st.write("")  # spacing placeholder
with row4[2]:
    st.write("")  # spacing placeholder
#with row4[3]:
    #predict_button = st.button("🔮 Predict", use_container_width=True)

# ------------------------------------------------------


# -----------------------------
# Prediction Logic
# -----------------------------

if st.button("🔮 Predict"):
    # Example encoding (replace with real preprocessing logic)
    # For now, just create a dummy input vector
    input_data = np.array([[age, gender, region, marital_status, bmi_category,
                            smoking_status, employment_status, income_level,
                            medical_history, insurance_plan]], dtype=object)

    # If model is available:
    # prediction = model.predict(input_data)
    # st.success(f"💵 Estimated Insurance Cost: ₹{prediction[0]:,.2f}")

    # For demo purpose: Random estimated cost (placeholder)
    import random
    random_cost = round(random.uniform(20000, 200000), 2)
    st.success(f"💵 Estimated Insurance Cost: ₹{random_cost:,.2f}")


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built by Patrick Ndabarishye")

