import streamlit as st
import pandas as pd
from helper import read_csv_autodelim

### Day 18 ###

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.txt'):
            st.info('Scherzkeks, wir können keine Textdateien lesen')
            st.subheader('Text File Content')
            st.write(uploaded_file.getvalue().decode("utf-8"))
        elif uploaded_file.name.endswith('.csv'):
            df = read_csv_autodelim(uploaded_file)#pd.read_csv(uploaded_file)
            st.subheader('DataFrame')
            st.write(df)
            st.subheader('Descriptive Statistics')
            st.write(df.describe())
        else:
            st.error(f"Hast Du sicher ein CSV hochgeladen, wir haben probleme beim Auslesen \n Error: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info('☝️ Upload a CSV')