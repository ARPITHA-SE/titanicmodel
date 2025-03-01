import streamlit as st
import joblib
import pandas as pd
model=joblib.load('titanic_model.pkl')
st.title('Titanic Model Frontend')
pcls=st.select_slider('Choose passenger class',[1,2,3])
age=st.slider('Input Age',0,100)
sib=st.slider('Input siblings',0,10)
parch=st.slider('Input parent/children',0,2)
fare=st.number_input('Fare Amount',0,100)
def predict_survivers():
    column_names=['Pclass','Age','Parch','Fare','SibSp']
    row=[pcls,age,parch,fare,sib]
    X=pd.DataFrame([row],columns=column_names)
    prediction=model.predict(X)
    if prediction==1:
        st.success('Passenger Servived')
    else:
        st.success('Passenger not survived')
st.button('Print',on_click=predict_survivers)
