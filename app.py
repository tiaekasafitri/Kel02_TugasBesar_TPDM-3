import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('resiko_obesitas.pkl','rb'))

# judul web
st.title('Prediksi Resiko Obesitas')

col1, col2, col3, col4 = st.columns(4)

with col1:
    calories = st.text_input('Kalori')
with col2:
    cholesterol = st.text_input('Kolesterol')
with col3:
    sodium = st.text_input('Natrium')
with col4:
    carbohydrates = st.text_input('Karbohidrat')
with col1:
    sugars = st.text_input('Gula')
with col2:
    protein = st.text_input('Protein')
with col3:
    vitamin = st.text_input('Vitamin')
with col4:
    calcium = st.text_input('Kalsium')
with col1:
    fat = st.text_input('Lemak')
with col2:
    iron = st.text_input('Zat Besi')
with col3:
    fiber = st.text_input('Serat')
with col4:
    potassium = st.text_input('Kalium')
with col1:
    minerals = st.text_input('Mineral')

# code for prediction
obesitas_diagnosis =''

# membuat tombol prediksi
if st.button('Prediksi Resiko Obesitas'):
    obesitas_prediction = model.predict([[calories,cholesterol,sodium,carbohydrates,sugars,protein,vitamin,calcium,fat,iron,fiber,potassium,minerals]])
    
    if (obesitas_prediction[0]==1):
        obesitas_diagnosis = 'Pasien Resiko Terkena Penyakit Obesitas'
    else:
        obesitas_diagnosis = 'Pasien Tidak Beresiko Terkena Penyakit Obesitas'
st.success(obesitas_diagnosis)