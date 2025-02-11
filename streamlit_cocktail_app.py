import streamlit as st
import requests
from random import randint

st.title('🍹 Cocktail API app')

def get_new_cocktail():
    suggested_cocktail_url = f'https://thecocktaildb.com/api/json/v1/1/filter.php?i={st.session_state.selected_ingredient}'
    json_data = requests.get(suggested_cocktail_url)
    st.session_state.suggested_cocktail = json_data.json()
    st.session_state.number_of_results = len(st.session_state.suggested_cocktail['drinks'])
    st.session_state.id = randint(0, st.session_state.number_of_results - 1)

st.sidebar.header('Input')
selected_ingredient = st.sidebar.selectbox(
    'Select an ingredient for a cocktail',
    ["Vodka", "Gin", "Rum", "Tequila", "Whiskey", "Brandy", "Cognac", "Vermouth", "Triple sec"],
    key='selected_ingredient',
    on_change=get_new_cocktail
)

if 'suggested_cocktail' not in st.session_state:
    get_new_cocktail()

suggested_cocktail_details_url = f'https://thecocktaildb.com/api/json/v1/1/lookup.php?i={st.session_state.suggested_cocktail["drinks"][st.session_state.id]["idDrink"]}'
json_data_details = requests.get(suggested_cocktail_details_url)
suggested_cocktail_details = json_data_details.json()

c1, c2, c3 = st.columns(3)
with c1:
    with st.expander('About this app'):
        st.write('Are you thirsty? The **Cocktail API app** provides suggestions on cocktails that you can make with your favorite ingredients. This app is powered by the Cocktail API.')
with c2:
    with st.expander('JSON data'):
        st.write(st.session_state.suggested_cocktail)
with c3:
    with st.expander('JSON data details'):
        st.write(suggested_cocktail_details)

st.write(f'Number of results: {st.session_state.number_of_results}')
st.write(f'Random id: {st.session_state.id}')

st.header('Suggested cocktail')
st.info(f"{st.session_state.suggested_cocktail['drinks'][st.session_state.id]['strDrink']} ({suggested_cocktail_details['drinks'][0]['strAlcoholic']})")

col1, col2 = st.columns([2, 1])
with col2:
    st.image(st.session_state.suggested_cocktail['drinks'][st.session_state.id]['strDrinkThumb'])
with col1:
    ingredients = [suggested_cocktail_details['drinks'][0][f'strIngredient{i}'] for i in range(1, 16) if suggested_cocktail_details['drinks'][0][f'strIngredient{i}']]
    measurements = [suggested_cocktail_details['drinks'][0][f'strMeasure{i}'] for i in range(1, 16) if suggested_cocktail_details['drinks'][0][f'strMeasure{i}']]
    st.subheader('Ingredients')
    for ingredient, measurement in zip(ingredients, measurements):
        st.write(f'- {ingredient} ({measurement})')

st.subheader('Instructions')
st.write(suggested_cocktail_details['drinks'][0]['strInstructions'])