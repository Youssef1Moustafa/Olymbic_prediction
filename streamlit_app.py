import streamlit as st
import pandas as pd
import pickle
import requests

# Google Drive direct download link (replace 'FILE_ID' with your actual ID)
drive_url = "https://drive.google.com/uc?export=download&id=1P4iQFeJ2anMm9It9JrUuOKbgDoKhMYaa"

# Function to download the model and check for HTML content
def download_model(url, filename="best_model.pkl"):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful

        # Check if the response content is HTML (indicates a problem)
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
