import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

# Load the model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Check if the loaded object is a valid model
if not hasattr(model, 'predict'):
    st.error("The loaded object is not a valid model!")
    st.stop()

# Streamlit app title
st.title("Sports Outcome Prediction")

# Input fields
noc = st.number_input("NOC", min_value=0, step=1)
country = st.number_input("Country", min_value=0, step=1)
sport = st.number_input("Sport", min_value=0, step=1)
event = st.number_input("Event", min_value=0, step=1)

# Prediction logic
if st.button("Predict Outcome"):
    input_data = pd.DataFrame([[noc, country, sport, event]], 
                              columns=['NOC', 'Country', 'Sport', 'Event'])
    
    prediction = model.predict(input_data)[0]
    result = 'Won' if prediction == 1 else 'Not Won'
    st.write(f"Predicted Outcome: {result}")

# Example DataFrame for the histogram (replace with your actual data)
data = {'Sport': ['Athletics', 'Swimming', 'Basketball', 'Football', 
                  'Gymnastics', 'Hockey', 'Tennis', 'Boxing', 'Wrestling', 'Cycling'],
        'count': [230, 150, 100, 120, 180, 140, 90, 80, 75, 110]}
top_sport = pd.DataFrame(data)

# Create Plotly histogram
fig = px.histogram(top_sport, x='Sport', y='count',
                   title='Top 10 Sports',
                   labels={'Sport': 'Sport', 'count': 'Count'})

# Display the chart in Streamlit
st.plotly_chart(fig)
