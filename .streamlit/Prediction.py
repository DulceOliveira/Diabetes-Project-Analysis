# importing libraries

import streamlit as st
import pickle
import pandas as pd


# Setting page configuration

st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="auto",)

# Custom the page CSS style

st.markdown(
    """
    <style>
    /* Custom Streamlit theme styles */
    h1 {
        color: #0E8992; /* Blue color for h1 (title) */
        font-size: 40px; /* Increase font size for h1 */
        font-weight: bold; /* Bold font for h1 */
    }

    h2 {
        color: #E9A27C; /* orange color for h2 (header) */
        font-size: 28px; /* Increase font size for h2 */
        font-style: italic; /* Italic style for h2 */
    }

    p {
        color: #333333; /* Dark gray color for text (p) */
        font-size: 14px; /* Increase font size for text (p) */
        font-weight: bold; /* Bold text for paragraphs */
    }

    /* Style buttons with an elegant color */
    .elegant-button {
        background-color: #1976D2; /* Blue background for buttons */
        color: white; /* White text for buttons */
        font-weight: bold; /* Bold text for buttons */
        padding: 10px 20px; /* Padding for buttons */
        border: none; /* Remove button border */
        border-radius: 5px; /* Add button border radius */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Displaying one image

image = st.image('https://www.channelislands.coop/media/236911/4137-diabetes-testing-content-banner.png?anchor=center&mode=crop&width=865&height=230&rnd=131945506110000000&format=jpg', width=700)

# Creating a title

st.title('Diabuddy: Raising Awareness 🩺')


# Create two columns for Personal Information section

name = st.text_input("Full Name", key="full_name")
email = st.text_input("Email Address", key="email")

# Defining the Streamlit widgets for user input

col1, col2 = st.columns(2)

# Creating dictionaries to map categorical variables

gender_mapping = {"Female": 0, "Male": 1}
yes_no_mapping = {"No": 0, "Yes": 1}
health_rating_mapping = {"Excellent": 1, "Very Good": 2, "Good": 3, "Fair": 4, "Poor": 5}
education_level_mapping = {"High School": 1, "College": 2, "Bachelor's Degree": 3, "Master's Degree": 4, "Doctorate": 5}

# Creating some organization, columns

with col1:
    High_Blood_Pressure = st.selectbox("High Blood Pressure?", ["No", "Yes"], key="High_Blood_Pressure")
    High_Cholesterol = st.selectbox("High Cholesterol?", ["No", "Yes"], key="High_Cholesterol")
    Cholesterol_Check = st.selectbox("Cholesterol Check", ["No", "Yes"], key="Cholesterol_Check")
    Smoking_Habit = st.selectbox("Do you smoke?", ["No", "Yes"], key="Smoking_Habit")
    Stroke_History = st.selectbox("Do you have stroke history?", ["No", "Yes"], key="Stroke_History")
    Heart_Disease_or_Attack_History = st.selectbox("Heart Disease or Attack History?", ["No", "Yes"], key="Heart_Disease_or_Attack_History")
    Physical_Activity_Level = st.selectbox("Do you practice physical activity", ["No", "Yes"], key="Physical_Activity_Level")
    Fruit_Consumption = st.selectbox("Do you consume fruit?", ["No", "Yes(1 or more per day)"], key="Fruit_Consumption")
    

with col2:
    Vegetable_Consumption = st.selectbox("Do you consume vegetables?", ["No", "Yes(1 or more per day)"], key="Vegetable_Consumption")
    Access_to_Healthcare = st.selectbox("Do you have access to healthcare", ["No", "Yes"], key="Access_to_Healthcare")
    No_Doctor_Bills_Covered_by_Cost = st.selectbox("No Doctor Bills Covered by Cost", ["No", "Yes"], key="No_Doctor_Bills_Covered_by_Cost")
    General_Health = st.selectbox("How is your health in general?", ["Excellent", "Very Good", "Good", "Fair", "Poor"], key="General_Health")
    Difficulty_Walking = st.selectbox("Do you have difficulty walking", ["No", "Yes"], key="Difficulty_Walking")
    Gender = st.selectbox("Gender", ["Female", "Male"], key="Gender")
    Age = st.text_input("Age", key="Age")
    Education_Level = st.selectbox("Education Level", ["High School", "College", "Bachelor's Degree", "Master's Degree", "Doctorate"], key="Education_Level")
    Body_Mass_Index = st.slider("Body Mass Index (BMI)", 10.0, 50.0, 25.0, 0.1, key="Body_Mass_Index")
    Physical_Health = st.slider("In the past 30 days, how many you weren't well physically?", 0, 30, 15, 1, key="Physical_Health")

# Creating a function to preprocess user inputs

def preprocess_inputs(High_Blood_Pressure, High_Cholesterol, Cholesterol_Check, Body_Mass_Index, Smoking_Habit, Stroke_History,
                      Heart_Disease_or_Attack_History, Physical_Activity_Level, Fruit_Consumption, Vegetable_Consumption,
                      Access_to_Healthcare, No_Doctor_Bills_Covered_by_Cost, General_Health, Physical_Health, Difficulty_Walking,
                      Gender, Age, Education_Level):
    # Map and convert categorical variables
    Gender = gender_mapping.get(Gender, -1)  # Default to -1 if not found
    High_Blood_Pressure = yes_no_mapping.get(High_Blood_Pressure, -1)
    High_Cholesterol = yes_no_mapping.get(High_Cholesterol, -1)
    Cholesterol_Check = yes_no_mapping.get(Cholesterol_Check, -1)
    Smoking_Habit = yes_no_mapping.get(Smoking_Habit, -1)
    Stroke_History = yes_no_mapping.get(Stroke_History, -1)
    Heart_Disease_or_Attack_History = yes_no_mapping.get(Heart_Disease_or_Attack_History, -1)
    Physical_Activity_Level = yes_no_mapping.get(Physical_Activity_Level, -1)
    Fruit_Consumption = yes_no_mapping.get(Fruit_Consumption, -1)
    Vegetable_Consumption = yes_no_mapping.get(Vegetable_Consumption, -1)
    Access_to_Healthcare = yes_no_mapping.get(Access_to_Healthcare, -1)
    No_Doctor_Bills_Covered_by_Cost = yes_no_mapping.get(No_Doctor_Bills_Covered_by_Cost, -1)
    General_Health = health_rating_mapping.get(General_Health, -1)
    Difficulty_Walking = yes_no_mapping.get(Difficulty_Walking, -1)
    Education_Level = education_level_mapping.get(Education_Level, -1)
    
    # Ensure Age is converted to an integer
    try:
        Age = int(Age)
    except ValueError:
        Age = -1  # Set to -1 if Age is not a valid integer

    inputs = {
        "High_Blood_Pressure": High_Blood_Pressure,
        "High_Cholesterol": High_Cholesterol,
        "Cholesterol_Check": Cholesterol_Check,
        "Body_Mass_Index": Body_Mass_Index,
        "Smoking_Habit": Smoking_Habit,
        "Stroke_History": Stroke_History,
        "Heart_Disease_or_Attack_History": Heart_Disease_or_Attack_History,
        "Physical_Activity_Level": Physical_Activity_Level,
        "Fruit_Consumption": Fruit_Consumption,
        "Vegetable_Consumption": Vegetable_Consumption,
        "Access_to_Healthcare": Access_to_Healthcare,
        "No_Doctor_Bills_Covered_by_Cost": No_Doctor_Bills_Covered_by_Cost,
        "General_Health": General_Health,
        "Physical_Health": Physical_Health,
        "Difficulty_Walking": Difficulty_Walking,
        "Gender": Gender,
        "Age": Age,
        "Education_Level": Education_Level
    }
    return inputs

# Preprocessing user inputs

user_inputs = preprocess_inputs(High_Blood_Pressure, High_Cholesterol, Cholesterol_Check, Body_Mass_Index, Smoking_Habit, Stroke_History,
                                Heart_Disease_or_Attack_History, Physical_Activity_Level, Fruit_Consumption, Vegetable_Consumption,
                                Access_to_Healthcare, No_Doctor_Bills_Covered_by_Cost, General_Health, Physical_Health, Difficulty_Walking,
                                Gender, Age, Education_Level)

# Displaying the preprocessed user inputs

st.subheader("Inserted Data:")
st.write(user_inputs)

# Loading the trained XGBoost model

model_filename = 'diabetes_project_model.pkl'
loaded_model = pickle.load(open(model_filename, 'rb'))

# Creating a function for diabetes prediction

def diabetes_prediction(input_data):
    # Convert the input data to a numpy array
    input_data_as_numpy_array = pd.DataFrame([input_data]).values

    # Making the prediction
    
    prediction = loaded_model.predict(input_data_as_numpy_array)

    if prediction[0] == 1:
        st.write("High risk of diabetes")
        st.write("You should consider consulting a healthcare professional for further evaluation. :wink:")
        st.write("Maintaining a healthy lifestyle and diet can help manage the risk.")
    else:
        st.write("Low risk of diabetes")
        st.write("Your risk of diabetes is low.🚴‍♀️")
        st.write("However, it's still essential to maintain a healthy lifestyle for overall well-being.")


# Adding a button to trigger the prediction

if st.button("Get Diabetes Prediction"):
    diagnosis = diabetes_prediction(user_inputs)
  
    

