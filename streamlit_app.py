import streamlit as st
import pandas as pd
import pickle
import requests
import gdown  # Ensure you have `gdown` installed

# Store the file ID from Google Drive
file_id = "1P4iQFeJ2anMm9It9JrUuOKbgDoKhMYaa"  # Replace with your actual Google Drive file ID

# Function to download the model and handle potential errors
def load_model_from_drive(file_id):
    output = 'vehicle_price_model.pkl'  # Save the model locally
    try:
        # Generate the download URL
        url = f'https://drive.google.com/uc?id={file_id}'
        
        # Download the file using gdown
        gdown.download(url, output, quiet=False)

        # Load the model
        with open(output, 'rb') as file:
            model = pickle.load(file)
        
        return model
    except Exception as e:
        st.error(f"Error loading the model: {str(e)}")
        return None  # Ensure this line is properly indented

# Load the model
model = load_model_from_drive(file_id)

# Stop the app if the model couldn't be loaded
if model is None:
    st.stop()

# Define the Streamlit app
st.title("Sports Outcome Prediction App")

st.write("Provide the following details to predict the outcome:")

# Input fields for prediction
noc = st.number_input("Enter NOC (Numeric Code for National Olympic Committee)", min_value=0, step=1)
country = st.text_input("Enter Country Name")
sport = st.text_input("Enter Sport Name")
event = st.text_input("Enter Event Name")

# Prediction logic
if st.button("Predict Outcome"):
    try:
        # Create a DataFrame from the input data
        input_data = pd.DataFrame(
            [[noc, country, sport, event]], 
            columns=['NOC', 'Country', 'Sport', 'Event']
        )

        # Show the input data for debugging
        st.write("Input Data Preview:", input_data)

        # Make a prediction using the model
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
