import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


np.random.seed(7)
dates = pd.date_range('2026-01-01','2026-12-31',freq='D')
cities = ['Delhi','Mumbai','Bengaluru']
categories = ['Electronics','Clothing','Grocery']

df = pd.DataFrame(
    [(d,c,k) for d in dates for c in cities for k in categories],
    columns=['Date','City','Category']
)

base = {'Electronics' : 400 ,'Clothing' : 250 ,'Grocery' : 150}
n=len(df)

df['Discount'] = np.random.choice([0,5,10,15,20],n)
trend = 1+ df['Date'].dt.dayofyear / 365 * 0.3
festive = np.where(df['Date'].dt.month.isin([10,11]),1.3,1.0)
weekend = np.where(df['Date'].dt.day_of_week >= 5,1.25,1.0)
city_factor = df['City'].map({'Delhi':1,'Mumbai':1.15,'Bengaluru':0.9})

df['Revenue'] = (df['Category'].map(base)*trend*weekend*festive*city_factor*(1+df['Discount']/100)*np.random.normal(1,0.08,n)).round(1)
df.loc[[100,1502,2801,],'Revenue']*=8

st.set_page_config(
    page_title='Retail Sales Dashboard',
    page_icon='',
    layout='wide'
)

st.title('Retail Sales Dashboard')
st.subheader('Assignment 5')
st.write('Visual Exploration of Retail Sales Data - 2026')