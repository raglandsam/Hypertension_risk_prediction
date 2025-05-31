import streamlit as st
import pandas as pd
import numpy as np

# Feature weights (based on your analysis)
weights = {
    'Age': 0.076,
    'BMI': 0.086,
    'Cholesterol': 0.082,
    'Systolic_BP': 0.078,
    'Diastolic_BP': 0.074,
    'Salt_Intake': 0.082,
    'Sleep_Duration': 0.075,
    'Stress_Level': 0.045,
    'Heart_Rate': 0.073,
    'Glucose': 0.082,
    'LDL': 0.082,
    'Triglycerides': 0.085,
    'HDL': 0.076
}

# Dummy means and stds (replace with actual data values if available)
means = {
    'Age': 45, 'BMI': 25, 'Cholesterol': 190, 'Systolic_BP': 120, 'Diastolic_BP': 80,
    'Salt_Intake': 4, 'Sleep_Duration': 7, 'Stress_Level': 3, 'Heart_Rate': 75,
    'Glucose': 100, 'LDL': 120, 'Triglycerides': 150, 'HDL': 50
}

stds = {
    'Age': 15, 'BMI': 5, 'Cholesterol': 30, 'Systolic_BP': 15, 'Diastolic_BP': 10,
    'Salt_Intake': 1, 'Sleep_Duration': 1.5, 'Stress_Level': 1, 'Heart_Rate': 10,
    'Glucose': 15, 'LDL': 25, 'Triglycerides': 40, 'HDL': 10
}

# Units for display
units = {
    'Age': 'years', 'BMI': 'kg/m²', 'Cholesterol': 'mg/dL', 'Systolic_BP': 'mmHg',
    'Diastolic_BP': 'mmHg', 'Salt_Intake': 'g/day', 'Sleep_Duration': 'hrs/day',
    'Stress_Level': '/10', 'Heart_Rate': 'bpm', 'Glucose': 'mg/dL',
    'LDL': 'mg/dL', 'Triglycerides': 'mg/dL', 'HDL': 'mg/dL'
}

# Standardization function
def standardize(val, mean, std):
    return (val - mean) / std if std != 0 else 0

# Risk scoring function
def hypertension_risk_score(features):
    score = 0
    for feature, weight in weights.items():
        z = standardize(features[feature], means[feature], stds[feature])
        score += z * weight
    scaled_score = ((score + 3) / 6) * 100  # Scale from -3 to +3 into 0 to 100
    return round(min(max(scaled_score, 0), 100), 2)

st.title("🩺 Hypertension Risk Score Estimator")
st.markdown("""
This app estimates your **Hypertension Risk Score** based on lifestyle, vitals, and blood test inputs. 
Results are visualized below with color-coded guidance.
""")

user_input = {}

# Input Fields using Expanders
tabs = st.tabs(["🫀 Vitals", "🍽️ Lifestyle", "🧪 Blood Tests"])

with tabs[0]:
    user_input['Age'] = st.slider("Age (years)", 0, 100, means['Age'], step=1)
    user_input['BMI'] = st.slider("BMI (kg/m²)", 10, 50, means['BMI'], step=1)
    user_input['Systolic_BP'] = st.slider("Systolic BP (mmHg)", 90, 200, means['Systolic_BP'], step=1)
    user_input['Diastolic_BP'] = st.slider("Diastolic BP (mmHg)", 60, 130, means['Diastolic_BP'], step=1)
    user_input['Heart_Rate'] = st.slider("Heart Rate (bpm)", 40, 150, means['Heart_Rate'], step=1)

with tabs[1]:
    user_input['Salt_Intake'] = st.slider("Salt Intake (g/day)", 0.0, 10.0, float(means['Salt_Intake']), step=0.5)
    user_input['Sleep_Duration'] = st.slider("Sleep Duration (hrs/day)", 0.0, 12.0, float(means['Sleep_Duration']), step=0.5)
    user_input['Stress_Level'] = st.slider("Stress Level (/10)", 0.0, 10.0, float(means['Stress_Level']), step=0.5)

with tabs[2]:
    user_input['Cholesterol'] = st.slider("Cholesterol (mg/dL)", 100, 300, means['Cholesterol'], step=1)
    user_input['Glucose'] = st.slider("Glucose (mg/dL)", 50, 200, means['Glucose'], step=1)
    user_input['LDL'] = st.slider("LDL (mg/dL)", 50, 250, means['LDL'], step=1)
    user_input['HDL'] = st.slider("HDL (mg/dL)", 20, 100, means['HDL'], step=1)
    user_input['Triglycerides'] = st.slider("Triglycerides (mg/dL)", 50, 300, means['Triglycerides'], step=1)

# Compute score and display
if st.button("🔎 Calculate Risk Score"):
    score = hypertension_risk_score(user_input)
    st.subheader(f"🧮 Your Estimated Hypertension Risk Score: {score}/100")
    st.progress(score / 100)

    if score < 30:
        st.success("🟢 Low Risk — Great! Keep up the healthy habits.")
    elif score < 70:
        st.warning("🟠 Moderate Risk — Consider reviewing diet, activity, and stress.")
    else:
        st.error("🔴 High Risk — Please consult a healthcare provider.")

    # Export report
    df_report = pd.DataFrame.from_dict(user_input, orient='index', columns=['Value'])
    df_report['Unit'] = df_report.index.map(units)
    df_report.reset_index(inplace=True)
    df_report.rename(columns={'index': 'Feature'}, inplace=True)
    df_report.loc[len(df_report.index)] = ['Risk Score', score, '/100']

    csv = df_report.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Your Report as CSV", data=csv, file_name="hypertension_report.csv", mime='text/csv')

