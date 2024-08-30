import streamlit as st
import numpy as np
import pickle

from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
scalar = pickle.load(open('scaler.pickle','rb'))
best_model = pickle.load(open('model.pickle','rb'))

st.title('Get a Home: Habitability Score Prediction (0 - 100)')

Power_Backup =st.selectbox("Does the property have a Power Backup",["Yes","No"])
Property_Area = st.number_input("What's the area of the property in square feets?",1,15000)
NR = st.number_input("On a scale of 1 (Low) to 5 (High), how would you rate the Neighborhood overall?", min_value=0.00, max_value=5.00, step=0.01, format="%.2f")
TDS = st.number_input("What is the Traffic Density score?", min_value=1.00, max_value=10.00, step=0.01, format="%.2f")
Furnishing = st.selectbox("What's the furnishing category for the property?",["Fully Furnished","Semi_Furnished","Unfurnished","Not Known"])
Crime_Rate  = st.selectbox("How would you categorize the Crime rate in the neighborhood?",["Well below average",
                                                                                     "Slightly below average",
                                                                                      "Slightly above average",
                                                                                      "Well above average"])
Furnishing_dict = {"Fully Furnished": 4,
    "Semi_Furnished": 3,
    "Unfurnished":2,
    "Not Known":1}

Crime_Rate_dict ={
      "Well below average":4,
    "Slightly below average":3,
    "Slightly above average":2,
    "Well above average":1
}
Furnishing = Furnishing_dict[Furnishing]
Crime_Rate = Crime_Rate_dict[Crime_Rate]

if Power_Backup == "Yes":
  Power_Backup = 1
else:
  Power_Backup = 0

Property_Area = np.log(Property_Area)

NR = (NR) * (NR)


data = [[Furnishing,Crime_Rate,Power_Backup,NR,Property_Area,TDS]]

scaled_data = scalar.transform(data)

result = best_model.predict(scaled_data)

result = result[0]

if st.button('Predict'):
  st.write("The Habitability Score is:", result)
