import streamlit as st
from datetime import time, datetime, timedelta

st.header('st.slider')

# Beispiel 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Beispiel 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

values = st.slider(
     'Select a range of values and set a step',
     0.0, 100.0, (25.0, 75.0), 1.0)
st.write('Lower bound value:', values[0], 'Upper bound value:', values[1])

# Beispiel 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))

start_time = datetime.combine(datetime.today(), appointment[0])
end_time = datetime.combine(datetime.today(), appointment[1])
duration = end_time - start_time

st.write("You're scheduled for a ", duration, " meeting at:", appointment[0])

# Beispiel 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)