import streamlit as st
import pandas as pd
import pickle
import os

# Load the model with error handling
model_path = 'est_model.pkl'
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    st.success("Model loaded successfully!")
else:
    st.error("Model file not found! Make sure 'model.pkl' is uploaded correctly.")
    st.stop()  # Stop the app if the model isn't found

# Define the Streamlit app
st.title("Sports Outcome Prediction")

st.write("Enter the following information to predict the outcome:")

# Input fields for the four features
noc = st.number_input("NOC Code", min_value=0, step=1)
country = st.number_input("Country Code", min_value=0, step=1)
sport = st.number_input("Sport Code", min_value=0, step=1)
event = st.number_input("Event Code", min_value=0, step=1)

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
