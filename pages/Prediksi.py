import pickle
import numpy as np
import streamlit as st



# Load model
model = pickle.load(open('kanker_logreg.sav','rb'))

# Judul
st.title('Prediksi Kanker Payudara dengan Logistic Regression')

# Slider dengan rentang yang disesuaikan
radius_mean = st.slider('Radius rata-rata', min_value=6.0, max_value=30.0, step=0.1)
texture_mean = st.slider('Texture rata-rata', min_value=9.0, max_value=40.0, step=0.1)
perimeter_mean = st.slider('Perimeter rata-rata', min_value=40.0, max_value=190.0, step=0.1)
area_mean = st.slider('Area rata-rata', min_value=150.0, max_value=2500.0, step=1.0)
smoothness_mean = st.slider('Smoothness rata-rata', min_value=0.05, max_value=0.20, step=0.001)
compactness_mean = st.slider('Compactness rata-rata', min_value=0.01, max_value=0.35, step=0.001)
concavity_mean = st.slider('Concavity rata-rata', min_value=0.0, max_value=0.45, step=0.001)
concave_points_mean = st.slider('Concave points rata-rata', min_value=0.0, max_value=0.20, step=0.001)
symmetry_mean = st.slider('Symmetry rata-rata', min_value=0.1, max_value=0.35, step=0.001)
fractal_dimension_mean = st.slider('Fractal dimension rata-rata', min_value=0.04, max_value=0.1, step=0.001)

radius_se = st.slider('Radius SE', min_value=0.1, max_value=3.0, step=0.1)
texture_se = st.slider('Texture SE', min_value=0.1, max_value=5.0, step=0.1)
perimeter_se = st.slider('Perimeter SE', min_value=0.5, max_value=25.0, step=0.1)
area_se = st.slider('Area SE', min_value=5.0, max_value=540.0, step=1.0)
smoothness_se = st.slider('Smoothness SE', min_value=0.001, max_value=0.05, step=0.001)
compactness_se = st.slider('Compactness SE', min_value=0.002, max_value=0.15, step=0.001)
concavity_se = st.slider('Concavity SE', min_value=0.0, max_value=0.4, step=0.001)
concave_points_se = st.slider('Concave points SE', min_value=0.0, max_value=0.05, step=0.001)
symmetry_se = st.slider('Symmetry SE', min_value=0.008, max_value=0.08, step=0.001)
fractal_dimension_se = st.slider('Fractal dimension SE', min_value=0.001, max_value=0.03, step=0.001)

radius_worst = st.slider('Radius worst', min_value=7.0, max_value=40.0, step=0.1)
texture_worst = st.slider('Texture worst', min_value=10.0, max_value=50.0, step=0.1)
perimeter_worst = st.slider('Perimeter worst', min_value=50.0, max_value=250.0, step=0.1)
area_worst = st.slider('Area worst', min_value=185.0, max_value=4250.0, step=1.0)
smoothness_worst = st.slider('Smoothness worst', min_value=0.07, max_value=0.25, step=0.001)
compactness_worst = st.slider('Compactness worst', min_value=0.02, max_value=1.5, step=0.001)
concavity_worst = st.slider('Concavity worst', min_value=0.0, max_value=1.2, step=0.001)
concave_points_worst = st.slider('Concave points worst', min_value=0.0, max_value=0.3, step=0.001)
symmetry_worst = st.slider('Symmetry worst', min_value=0.1, max_value=0.6, step=0.001)
fractal_dimension_worst = st.slider('Fractal dimension worst', min_value=0.05, max_value=0.2, step=0.001)

# Kode Prediksi
cancer_diagnosis = ''

# Tombol Prediksi
if st.button('Prediksi'):
    cancer_prediction = model.predict([[ 
        radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean,
        concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se,
        smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, 
        texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, 
        symmetry_worst, fractal_dimension_worst 
    ]])
    
    if cancer_prediction[0] == 1:
        cancer_diagnosis = 'Anda Terkena Kanker Payudara Ganas'
    else:
        cancer_diagnosis = 'Anda Terkena Kanker Payudara Jinak'

st.success(cancer_diagnosis)
