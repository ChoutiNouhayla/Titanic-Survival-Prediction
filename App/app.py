import streamlit as st
import joblib
import pandas as pd

# Load your saved model (upload the .pkl file to Colab first or train it in the same notebook)
model = joblib.load('/content/drive/MyDrive/titanic-project/Models/titanic_random_forest_model.pkl')

st.title("Titanic Survival Prediction App")

st.markdown("Enter passenger information to predict survival.")

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 0, 100, 30)

with col2:
    fare = st.number_input("Fare paid", 0.0, 1000.0, 50.0)
    embarked = st.selectbox("Port of Embarkation", ["S (Southampton)", "C (Cherbourg)", "Q (Queenstown)"])
    family_size = st.slider("Family Size (including self)", 1, 11, 1)

# Map inputs to model format
sex_val = 1 if sex == "Female" else 0
embarked_val = 0 if embarked.startswith("S") else 1 if embarked.startswith("C") else 2
is_alone = 1 if family_size == 1 else 0

input_df = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex_val],
    'Age': [age],
    'Fare': [fare],
    'Embarked': [embarked_val],
    'FamilySize': [family_size],
    'IsAlone': [is_alone]
    # Add other features if your model needs them (SibSp, Parch...)
})

if st.button("Predict Survival"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.success(f"**Survived** with probability {probability:.1%} 🎉")
    else:
        st.error(f"**Did NOT survive** – survival probability {probability:.1%}")
