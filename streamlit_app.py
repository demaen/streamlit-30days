import streamlit as st
import pandas as pd
from helper import read_csv_autodelim




### DAY 19 ###

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')



### Day 18 ###

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.txt'):
            st.info(user_name, ' du Scherzkeks, wir können keine Textdateien lesen')
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
    st.info('☝️ ' + ', '.join(filter(None, [user_name, 'upload a CSV', user_emoji])))
