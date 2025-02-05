import streamlit as st
import pandas as pd
import numpy as np
import altair as alt



# Header und Selectbox
st.header('st.selectbox')
color_array = ['Blue', 'Red', 'Green']
pantone_colors = {
    "Blue": "#0033A0",   # Beispiel: Pantone 286 C
    "Red": "#DA291C",    # Beispiel: Pantone 485 C
    "Green": "#009639",   # Beispiel: Pantone 347 C
    "Yellow": "#FFD700",  # Beispiel: Pantone 109 C
}
# Dynamische Erstellung des Range-Arrays, indem für jeden Wert in color_array der entsprechende Hex-Code aus dem Dictionary abgefragt wird
color_range = [pantone_colors[color] for color in color_array]


### DAY 10 ###

# indem wir st.selectbox einer vaiablen zuweisen, können wir den Wert später verwenden
option = st.selectbox(
    'What is your favorite color?',
    color_array
)

st.write('Your favorite color is ', option)

st.write('Pantone color code:', pantone_colors[option])

# mit index kann ein Standardwert festgelegt werden
st.selectbox('Select a color:', color_array, index=2)

### DAY 11 ###
st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'], # Standardwerte
     max_selections=2) # Maximale Anzahl an auswählbaren Optionen
    

st.write('You selected:', options)


### DAY 9 ###

# Header für das Liniendiagramm
st.header('Line chart')

# Erzeugen eines DataFrames mit zufälligen Daten
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=color_array
)

# Umformen des DataFrames in ein "long"-Format, damit Altair die Daten gruppieren kann
chart_data_long = chart_data.reset_index().melt(id_vars='index', 
                                                var_name='color', 
                                                value_name='value')

# Definieren einer Farbschlüsselung (Scale), die den Spaltennamen die entsprechenden Farben zuweist
color_scale = alt.Scale(
    domain=color_array,
    range=color_range
)

# Erstellen des Altair-Diagramms: 
# - x-Achse: der Index (hier als Zeit oder Reihenfolge zu verstehen)
# - y-Achse: die Werte
# - color: Die Spalte "color" wird gemäß der definierten Farbschlüsselung eingefärbt.
chart = alt.Chart(chart_data_long).mark_line().encode(
    x=alt.X('index:Q', title='Index'),
    y=alt.Y('value:Q', title='Value'),
    color=alt.Color('color:N', scale=color_scale, title='Color')
).properties(
    width=600,
    height=400,
    title="Line Chart mit benutzerdefinierten Farben"
)

st.altair_chart(chart, use_container_width=True)

### DAY 12 ###
st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee', value=True)
cola = st.checkbox('Cola')
lemonade = st.checkbox('Lemonade', disabled = ("Red" in option), label_visibility = "collapsed" if "Green" in option else "visible") # label hat ein komisches Verhalten, wenn es auf "collapsed" gesetzt wird, da dann die checkbox weiterhin angezeigt wird, aber das label nicht mehr sichtbar ist

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some tasty coffee ☕")

if cola:
     st.write("Here you go 🥤")
