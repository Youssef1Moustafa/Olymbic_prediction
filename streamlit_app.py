import streamlit as st
import pandas as pd
import pickle

# Load your saved model (ensure 'model.pkl' is in the same directory or provide the correct path)
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the Streamlit app
st.title("Medals Prediction")

st.write("Enter the following information to predict the outcome:")

# Input fields for the four features
noc = st.number_input("NOC Code", min_value=0, step=1)
country = st.number_input("Country Code", min_value=0, step=1)
sport = st.number_input("Sport Code", min_value=0, step=1)
event = st.number_input("Event Code", min_value=0, step=1)

# Button to make prediction
if st.button("Predict Outcome"):
    # Prepare the input data as a DataFrame
    input_data = pd.DataFrame([[noc, country, sport, event]], 
                              columns=['NOC', 'Country', 'Sport', 'Event'])

    # Make prediction using the model
    prediction = model.predict(input_data)[0]

    # Display the result
    st.write(f"Predicted Outcome: {'Won' if prediction == 1 else 'Not Won'}")
