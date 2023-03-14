# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:18:05 2023

@author: Sarah Ahmed
"""

import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('heartdiseaseprediction.sav', 'rb'))


#prediction function

def heart_prediction(data_input):
    

 #converting input to numpy array easier for reshaping
 
    input_numpy= np.asarray(data_input)

#reshaping array helps make prediction for one value not all the 223 values
#tells ML model that prediction is for one value

    reshape_input = input_numpy.reshape(1,-1)

    predictionsystem =model.predict(reshape_input)
    print(predictionsystem)

    if (predictionsystem[0] == 0):
      return 'CONGRATULATIONS! you have no heart disease'
    else:
      return 'unfortunately you have heart disease , it is advised you book an appointment with a cardiologist in the app for immediate treatment'
  
    
  
def main():
    

    st.title('welcome to MediHelp heart Prediction')
    
    age = st.text_input('enter your age')
    gender = st.text_input(' enter your gender Female = 0 , Male = 1 ')
    chestpain = st.text_input('enter your level of chest pain 0 = no chest pain , 1 = typical , 2 = atypical , 3 = non angina pain')
    trestbps = st.text_input('enter your resting blood pressure')
    cholestrol = st.text_input('enter your your cholestrol')
    fbs = st.text_input('is your fasting blood sugar higher than 120 ? 0 = no , 1 = yes')
    thalach = st.text_input('enter your maximum heart rate')
    exerciseangina =st.text_input('Do you have exercise induced angina ? 0 = no , 1 = yes')
    oldpeak = st.text_input('enter your old peak value 0 to 6 , 6 being the highest old peak')
    Thalassemia= st.text_input('enter your thalassemia value 0 to 3 , 3 being the highest thalassemia ')


    diagnosebyML = ''
    
    # prediction button
    
    if st.button('heart prediction Test Result'):
           diagnosebyML = heart_prediction([ age, gender, chestpain, trestbps,cholestrol , fbs, thalach, exerciseangina,oldpeak, Thalassemia])
           
           
    st.success(diagnosebyML)
       
    
    
if __name__ == '__main__':
    main()