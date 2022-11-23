import streamlit as st
import pickle
import numpy as np

st.title('LAPTOP PRICE PREDICTOR')
model = pickle.load(open('pipe1.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

#Brand

company = st.selectbox('Brand',df['Company'].unique())

#Type of laptop

Type = st.selectbox('Type',df['TypeName'].unique())

#RAM

Ram = st.selectbox('RAM(IN GB)',[2,4,6,8,12,16,24,32,64])

#Weight
weight = st.number_input('Weight of Laptop')

#Touchscreen

Touchscreen = st.selectbox('Touchscree',['No',"Yes"])

# IPS
ips = st.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu = st.selectbox('CPU',df['Cpu_Brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if Touchscreen == 'Yes':
        Touchscreen = 1
    else:
        Touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,Type,Ram,weight,Touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(model.predict(query)[0]))))

