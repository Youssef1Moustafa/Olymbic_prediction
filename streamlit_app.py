import streamlit as st
import pandas as pd
import pickle
import requests

# Google Drive direct download link (replace 'FILE_ID' with your actual ID)
drive_url = "https://drive.google.com/uc?export=download&id=1P4iQFeJ2anMm9It9JrUuOKbgDoKhMYaa"  

# Function to download and save the model locally
def download_model(url, filename="best_model.pkl"):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful

        # Save the model locally
        with open(filename, "wb") as f:
            f.write(response.content)

        return filename
    except requests.exceptions.RequestException as e:
        st.error(f"Error downloading the model: {e}")
        st.stop()

# Download and load the model
st.write("Loading the model...")
model_filename = download_model(drive_url)

try:
    with open(model_filename, "rb") as f:
        model = pickle.load(f)
    st.success("Model loaded successfully!")
except pickle.UnpicklingError as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

# Define the Streamlit app
st.title("Sports Outcome Prediction")
st.write("Enter the following information to predict the outcome:")

# Input fields for the four features
noc = st.number_input("NOC", min_value=0, step=1)
country = st.number_input("Country", min_value=0, step=1)
sport = st.number_input("Sport", min_value=0, step=1)
event = st.number_input("Event", min_value=0, step=1)

# Make sure inputs are valid before making a prediction
if st.button("Predict Outcome"):
    try:
        # Prepare the input data as a DataFrame
        input_data = pd.DataFrame([[noc, country, sport, event]], 
                                  columns=['NOC', 'Country', 'Sport', 'Event'])

        # Debugging: Print input data to ensure it's correct
        st.write("Input Data:", input_data)

        # Make prediction using the model
        prediction = model.predict(input_data)[0]

        # Display the result
        st.write(f"Predicted Outcome: {'Won' if prediction == 1 else 'Not Won'}")

    except AttributeError as e:
        st.error(f"Prediction failed: {e}")
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
