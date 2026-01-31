# Titanic Survival Prediction – End-to-End Data Science Project

![Titanic Header](images/titanic_header.jpg) <!-- add a nice header image -->

Predicting passenger survival on the Titanic using machine learning — full project including EDA, interactive Tableau dashboards, model training, evaluation, and Streamlit deployment.

## Project Overview

This project analyzes the famous Titanic dataset to:
- Understand passenger demographics
- Visualize survival patterns
- Build and compare ML models
- Deploy an interactive prediction app

## Table of Contents

- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Tableau Dashboards](#tableau-dashboards)
- [Machine Learning Modeling](#machine-learning-modeling)
- [Interactive Streamlit App](#interactive-streamlit-app)
- [Results](#results)
- [How to Run Locally](#how-to-run-locally)
- [Future Improvements](#future-improvements)

## Technologies

- Python, Pandas, Scikit-learn, Matplotlib, Seaborn
- Tableau Public (interactive dashboards)
- Streamlit (web app deployment)
- Joblib (model saving)

## Tableau Dashboards

Three interactive dashboards published on Tableau Public:

1. **Overview** – High-level summary  
   → [View Dashboard](https://public.tableau.com/app/profile/nouhayla.chouti/viz/Overview_Dashboard_17691809282820/OverviewDashboard1)  

2. **Demographics** – Who was on board?  
   → [View Dashboard](https://public.tableau.com/app/profile/nouhayla.chouti/viz/DemographicsDashboard_17691811531120/DemographicsDashboard)  

3. **Survival Analysis** – What factors influenced survival?  
   → [View Dashboard](https://public.tableau.com/app/profile/nouhayla.chouti/viz/titanicDashboard1/SurvivalAnalysisdashboard#1)  

(Screenshots in `/Dashboards/Screenshot/`)

## Machine Learning Modeling

- Best model: **Random Forest** – Accuracy ~83% on test set
- Key features: Sex (gender), Pclass, Age, Fare
- Notebook: [`03_Modeling_and_Evaluation.ipynb`](Notebook/03_Modeling_and_Evaluation.ipynb)

Feature Importance:

![Feature Importance](Photos/Feature_Importance.png)

## Interactive Streamlit App

Live demo: [Titanic Survival Predictor](https://your-streamlit-url.streamlit.app)  
(or run locally – see below)

![Streamlit App Screenshot](App/screenshots/app_screenshot.png)

## How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/ChoutiNouhayla/Titanic-Survival-Prediction.git
   cd Titanic-Survival-Prediction
