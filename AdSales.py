import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib as plt
import joblib
import warnings
warnings.filterwarnings('ignore')
#import plotly.express as px

data = pd.read_csv('AdvertAndSales.csv')

st.markdown("<h1 style = 'color: #DD5746; text-align: center; font-size: 60px; font-family: Monospace'>ADVERT SALES PREDICTOR</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #FFC470; text-align: center; font-family: Serif '>Built by MATTHEW</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html=True)

st.image('pngwing.com (1).png')
st.divider()

st.markdown("<h2 style = 'color: #F7C566; text-align: center; font-family: montserrat '>Background Of Study</h2>", unsafe_allow_html = True)
st.markdown('Advertising plays a pivotal role in shaping consumer awareness and driving sales. Businesses allocate significant resources to advertising, aiming to reach target audiences and communicate value propositions effectively. However, quantifying the direct impact of advertising on sales performance remains a challenge, with debates surrounding its cost-effectiveness and long-term benefits. Understanding the relationship between advertising efforts and sales outcomes is essential for optimizing marketing strategies and ensuring a positive return on investment (ROI). This study seeks to examine how advertising influences consumer purchasing behavior and contributes to sales growth, providing actionable insights for businesses to maximize their marketing efficiency.')
st.divider()

st.dataframe(data, use_container_width=True )

st.sidebar.image('pngwing.com_user_icon.png', caption='Welcome User')

tv = st.sidebar.number_input('Television advert exp', min_value=0.0, max_value=10000.0, value=data.TV.median())
radio = st.sidebar.number_input('Radio advert exp', min_value=0.0, max_value=10000.0, value=data.Radio.median())
socials = st.sidebar.number_input('Social media advert exp', min_value=0.0, max_value=10000.0, value=data['Social Media'].median())
infl = st.sidebar.selectbox('Type of influencer', data.Influencer.unique(), index =1)

#user input
inputs = {
    'TV': [tv],
    'Radio': [radio],
    'Social Media' : [socials],
    'Influencer' : [infl]
}

inputVar = pd.DataFrame(inputs)
st.divider()
st.header("User Input")
st.dataframe(inputVar)

# Transform user inputs
Influencer_encoder = joblib.load('Influencer_encoder.pki')

# use the transformer to transform the user input
inputVar['Influencer'] = Influencer_encoder.transform(inputVar[['Influencer']])

#Bring in the model
model = joblib.load('advertmodel.pki')

predictbutton = st.button('Push to predict the Sales')

if predictbutton:
    predicted = model.predict(inputVar)
    st.success(f'the predicted Sales value is:  {predicted}')
