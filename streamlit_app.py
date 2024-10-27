import streamlit as st
import pandas as pd
import pickle
import requests

# Store the file ID from Google Drive
file_id = "1P4iQFeJ2anMm9It9JrUuOKbgDoKhMYaa"  # Replace with your actual Google Drive file ID

# Create the direct download link
drive_url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Function to download the model and handle potential errors
def download_model(url, filename="best_model.pkl"):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful

        # Check if the content is HTML (indicating an error or permission issue)
        if response.content[:6] == b'<html>':
            st.error("Failed to download the model. Check the link or permissions.")
            st.stop()

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
st.title("Sports Outcome Prediction App")

st.write("Provide the following details to predict the outcome:")

# Customized input fields for prediction
noc = st.number_input("Enter NOC (Numeric Code for National Olympic Committee)", min_value=0, step=1)
country = st.text_input("Enter Country Name")
sport = st.text_input("Enter Sport Name")
event = st.text_input("Enter Event Name")

# Ensure inputs are valid before making a prediction
if st.button("Predict Outcome"):
    try:
        # Create a DataFrame from the input data
        input_data = pd.DataFrame(
            [[noc, country, sport, event]], 
            columns=['NOC', 'Country', 'Sport', 'Event']
        )

        # Debugging: Show the input data on the app
        st.write("Input Data Preview:", input_data)

        # Make a prediction using the loaded model
        prediction = model.predict(input_data)[0]

        # Display the prediction result
        if prediction == 1:
            st.success("Prediction: The team/player is likely to WIN!")
        else:
            st.warning("Prediction: The team/player may NOT win.")

    except AttributeError as e:
        st.error(f"Prediction failed: {e}")
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
