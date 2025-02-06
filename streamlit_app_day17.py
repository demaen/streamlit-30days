import streamlit as st

### DAY 15 ###

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r_2^3 + \cdots + a r_{n-2}^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

### DAY 16 ###

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#000000"
backgroundColor="#000000"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number*12)

text = st.sidebar.text_input('Enter a text wit a number:', number)

### DAY 17 ###
st.title('st.secrets')

st.write(st.secrets['message'])

st.write("nicht verraten! " + ", ".join([st.secrets['geheimnis'][x] for x in st.secrets['geheimnis']]))
