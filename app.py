import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import RobustScaler
from scipy.stats import boxcox
from sklearn.ensemble import RandomForestRegressor
scalar = pickle.load(open('/content/drive/MyDrive/scaler.pickle','rb'))
best_model = pickle.load(open('/content/drive/MyDrive/best_model.pickle','rb'))


st.title('Get a Home: Habitability Score Prediction (0 - 100)')
Power_Backup = st.selectbox("Does the property have a Power Backup?",["Yes","No"])

Furnishing=st.selectbox("What Furnishing Category the property falls in?",
                          ["Fully Furnished","Semi_Furnished","Unfurnished","No Preference"])
Crime_Rate  = st.selectbox("How's the Crime Rate in the neighborhood?",
                           ["Well below average","Slightly below average","Slightly above average","Well above average"])
Water_Supply  = st.selectbox("What's the Water supply frequency?",
                           ["All time","No Preference","Once in a day - Evening","Once in a day - Morning","Once in two days"])
Property_Area = st.number_input("What's the area of the property in square feets?",1,15000)
NR = st.number_input("On a scale of 1 (Low) to 5 (High), how would you rate the Neighborhood overall?", min_value=1.00, max_value=5.00, step=0.01, format="%.1f")

TDS = st.number_input("What's the Traffic Density Score?", min_value=1.00, max_value=10.00, step=0.01, format="%.1f")
if Power_Backup == "Yes":
  Power_Backup = 1
else:
  Power_Backup = 0

Furnishing_dict = {'Fully Furnished': 81.06981290069344,
 'Semi_Furnished': 75.48216861477245,
 'Unfurnished': 63.85611257953989,
 'No Preference': 73.57988304093568}

Furnishing = Furnishing_dict[Furnishing]

Crime_rate_dict = {'Slightly above average': 64.91923607122344,
 'Slightly below average': 73.56087397308163,
 'Well above average': 54.99572961373391,
 'Well below average': 77.82694758427529}

Crime_Rate = Crime_rate_dict[Crime_Rate]

Water_supply_dict = {'All time': 75.80058038727094,
 'No Preference': 73.97781710914454,
 'Once in a day - Evening': 70.1841603004014,
 'Once in a day - Morning': 73.19230532786885,
 'Once in two days': 64.78702731092437}

Water_Supply = Water_supply_dict[Water_Supply]



Property_Area = np.log(Property_Area)

NR = np.log(NR)


data = [[Furnishing,Power_Backup,Crime_Rate,Water_Supply,NR,Property_Area,TDS]]

scaled_data = scalar.fit_transform(data)

result = best_model.predict(scaled_data)



if st.button('Predict'):
  st.write("The Habitability Score is:", result[0])
