# AIRLINE PASSENGER SATISFACTION PREDICTION
This project utilizes the Random Forest algorithm to predict passenger satisfaction with an airline based on key flight experience factors. By analyzing features like flight distance, inflight entertainment, and seat comfort, the model provides valuable insights for improving customer experiences and service quality in the aviation industry.

## Table of Contents:
* Objectives
* IDE
* Libraries
* Libraries Installation
* Dataset
* Methodology
* Streamlit for Model Deploymet
* Streamlit Installation
* Steps for model deployment
* App Link

## Objectives:
This project aims to predict passenger satisfaction with an airline based on various features and attributes. 

The prediction is made using the Random Forest algorithm, a powerful ensemble learning technique.

## IDE:
Google Colaboratory
## Libraries for Model Development:

* Pandas
* Numpy
* Matplotlib
* Scikit-learn
## Libraries Installation:

1.Pandas 
```bash
  pip install pandas
```
2.Numpy
```bash
  pip install numpy
```
3.Matplotlib
```bash
  pip install matplotlib
```
4.Scikit Learn
```bash
  pip install scikit-Learn
```
## Dataset:
The Airline Passenger Satisfaction Prediction Dataset has been used for this purpose, taken from the Kaggle*. link is below.

* [Dataset](https://www.kaggle.com/code/khatiba/airline-passenger-satisfaction-random-forest/input)

## Methodology:

The project follows these steps:

* **Data Preprocessing**: Cleaning, handling missing values, and encoding categorical variables.
* **Data Exploration**: Exploratory Data Analysis (EDA) to understand the relationships between features and passenger satisfaction.
* **Model Building**: Implementing the Random Forest algorithm for prediction.
* **Model Evaluation**: Assessing the model's performance using appropriate metrics.
* **Deployment**: Deploying the model using Streamlit for user interaction.

## STREAMLIT FOR MODEL DEPLOYMENT:

Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. It is a Python-based library specifically designed for machine learning engineers.Streamlit allows you to create a stunning-looking application with only a few lines of code.

* [Streamlit](https://streamlit.io/)-website

## Streamlit Installation:
```bash
  pip install streamlit
```

## Steps for Model Deployment:

**Step 1**: Organize machine learning code into a script or module that loads your trained model and makes predictions. Ensure that code is working correctly and produces the desired outputs.

**Step 2**: Create a new Python script or module for Streamlit app. Import the necessary libraries, including Streamlit, and define the structure of your app.

**Step 3**: Use Streamlit's API to design the user interface of the app. Streamlit provides various components such as sliders, dropdowns, and buttons that you can use to create interactive elements for user input and display.

**Step 4**: **Load the model**
In Streamlit app, load the trained machine learning model that we want to deploy. Make sure to import any required dependencies and set up any preprocessing steps needed to prepare input data for the model.

**Step 5**: **Define the prediction logic**
Write the code that takes user input, preprocesses it if necessary, and passes it to the loaded model for prediction. Capture the model's output and display it to the user.

**Step 6**: Run the Streamlit app using the below command
```bash
  streamlit run Campus_Placement_Prediction_app.py
```

**Step 7**: **Test the app** 
Interact with app in the web browser to ensure that everything is functioning as expected. Test different inputs and verify that the predictions are accurate.

## App Link:
[APP](https://airline-passenger-satisfaction-prediction-uza3knrzn8uqhcmnqfcd.streamlit.app/)

### THANK YOU FOR VISITING MY PROJECT
