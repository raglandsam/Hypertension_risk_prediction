🌺 Hypertension Risk Analysis & Prediction

This is a miniature project on analyzing the blood pressure metrics , cholesterol and other health factors of 
over 180,000 people and predicting hypertension in individuals. 

It features:

	* A full preprocessing pipeline built in Google Colab
	* Statistical and Machine learning models trained on a 180K+ health dataset
	* A Streamlit app to estimate individual hypertension risk scores


----
📂 Project Structure: 


HypertensionRiskProject/
│
├── notebooks/
│   └── preprocessing_and_modelling.ipynb
│
├── app/
│   └── hypertension_app.py
│
├── source_data/
│   └── health_dataset.csv
│
├── README.md
└── requirements.txt
```

---

📊 Features Used :
	These ae the various health related attributes of people from the dataset

* Age (years)
* BMI (kg/m^2)
* Systolic & Diastolic BP (mmHg)
* Cholesterol (mg/dL)
* Glucose (mg/dL)
* LDL, HDL, Triglycerides (mg/dL)
* Heart Rate (bpm)
* Sleep Duration (hrs)
* Stress Level, Salt Intake (scaled 0-10)
---


Running the Streamlit App:

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit application
streamlit run app/hypertension_app.py

App link ! -->  https://hypertensionriskprediction-8fn7uzqs9ucy3urb953t3l.streamlit.app/


---

🧠 Models Used :
    In order to conclude the strongest correlations between the attributes of the dataset , and to conclude the attributes contributing the most to hypertension,
    few statistical and machine learning models were used , which are:


	* Logistic Regression
	* Random Forest
	* XGBoost
	* Naive Bayes
	* Linear SVC
	* Combined model (averaged feature importance)

---

🔬 Notebooks

The preprocessing notebook includes:

* Data cleaning & null handling
* Label encoding & scaling
* Correlation heatmaps & feature plots
* Model training & evaluation
* Feature importance extraction

> [Colab Notebook Link](https://colab.research.google.com/drive/1N6xGsqU0bZb5v3SlhMRRwR3tcpxKkkN9?usp=sharing)

---

📄 Requirements

All dependencies are listed in `requirements.txt`, including:

*  pandas
*  scikit-learn
*  xgboost
*  streamlit
*  matplotlib
*  seaborn
*  scipy ( for pearson's correlation test)
*  Numpy

---

🎯 Future Improvements

* Add severity scoring with category breakdown
* Personalized health & lifestyle suggestions
* Downloadable PDF reports from app
* Streamlit Cloud deployment

---

👤 Author ?

Built with ❤️ by Samuel Ragland

THANKS!
