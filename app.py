import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn


pickle_in = open('randomforestclassifier.pkl','rb')

model = pickle.load(pickle_in)


st.title("Credit Card Fraud Detection") 



# inputting a variable
V1= st.number_input("Enter the input for V1")
V2= st.number_input("Enter the input for V2")
V3= st.number_input("Enter the input for V3")
V4= st.number_input("Enter the input for V4")
V5= st.number_input("Enter the input for V5")
V6= st.number_input("Enter the input for V6")
V7= st.number_input("Enter the input for V7")
V8= st.number_input("Enter the input for V8")
V9= st.number_input("Enter the input for V9")
V10= st.number_input("Enter the input for V10")
V11= st.number_input("Enter the input for V11")
V12= st.number_input("Enter the input for V12")
V13= st.number_input("Enter the input for V13")
V14= st.number_input("Enter the input for V14")
V15= st.number_input("Enter the input for V15")
V16= st.number_input("Enter the input for V16")
V17= st.number_input("Enter the input for V17")
V18= st.number_input("Enter the input for V18")
V19= st.number_input("Enter the input for V19")
Amount= st.number_input("Enter the input for Amount")
submit = st.button("predict")
# Convert prediction to a human-readable response
if submit:
    prediction = model.predict([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,Amount]])
    if prediction == 1:
        st.write("Fraudulent transaction")
    else:
        st.write("Legitimate transaction")
    
        
        
        
        
        
        
        
        
        
        
        
        