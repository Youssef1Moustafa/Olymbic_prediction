import streamlit as st
import pandas as pd
import pickle
import gdown

# Google Drive File ID (replace with your file ID)
file_id = "1P4iQFeJ2anMm9It9JrUuOKbgDoKhMYaa"

# Function to download the model
def load_model_from_drive(file_id):
    output = 'best_model.pkl'
    try:
        url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(url, output, quiet=False)
        with open(output, 'rb') as file:
            model = pickle.load(file)
        # Check if the loaded model is a valid scikit-learn model
        if not hasattr(model, 'predict'):
            raise ValueError("Loaded model is not a valid scikit-learn model.")
        return model
    except Exception as e:
        st.error(f"Error loading the model: {str(e)}")
        return None

# Load the model
model = load_model_from_drive(file_id)

# Stop the app if the model couldn't be loaded
if model is None:
    st.stop()

# Define the category-to-number encoders (example mappings)
country_mapping = {'USA': 0, 'UK': 1, 'Japan': 2, 'Egypt': 3}
sport_mapping = {'Basketball': 0, 'Soccer': 1, 'Swimming': 2}
event_mapping = {'Final': 0, 'Semi-Final': 1, 'Quarter-Final': 2}

# Define the Streamlit app
st.title("Sports Outcome Prediction App")

# Collect user inputs
noc = st.number_input("Enter NOC (Numeric Code for National Olympic Committee)", min_value=0, step=1)

country = st.selectbox("Select Country", options=country_mapping.keys())
sport = st.selectbox("Select Sport", options=sport_mapping.keys())
event = st.selectbox("Select Event", options=event_mapping.keys())

# Convert categorical inputs to numerical values using the mappings
country_encoded = country_mapping[country]
sport_encoded = sport_mapping[sport]
event_encoded = event_mapping[event]

# Prediction logic
if st.button("Predict Outcome"):
    try:
        # Prepare the input data
        input_data = pd.DataFrame(
            [[noc, country_encoded, sport_encoded, event_encoded]],
            columns=['NOC', 'Country', 'Sport', 'Event']
        )

        # Show input data for debugging purposes
        st.write("Input Data Preview:", input_data)

        # Make a prediction using the loaded model
        prediction = model.predict(input_data)[0]  # Ensure prediction is called on the model

        # Display the prediction result
        if prediction == 1:
            st.success("Prediction: The team/player is likely to WIN!")
        else:
            st.warning("Prediction: The team/player may NOT win.")

    except ValueError as ve:
        st.error(f"Prediction failed: {ve}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
