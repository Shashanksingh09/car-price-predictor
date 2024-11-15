import streamlit as st
import pandas as pd
import joblib


model = joblib.load('Assignment1.pkl')

# Streamlit app
st.title('Car Price Predictor')

model_year=st.number_input("Model Year")
distance_covered=st.number_input("distance_covered (km)")
maker=st.selectbox("maker",['Audi', 'BMW','Chevrolet', 'Datsun', 'Fiat', 'Ford',
       'Honda', 'Hyundai', 'Jeep', 'KIA', 'MG',
       'Mahindra', 'Maruti', 'Mercedes', 'Nissan',
       'Renault', 'Skoda', 'Ssangyong', 'Tata',
       'Toyota', 'Volkswagen', 'Volvo'])
fuel_type=st.selectbox("fuel_type",['Diesel',
       'Electric', 'Petrol', 'Petrol + CNG',
       'Petrol + LPG'])
pre_owner=st.selectbox("pre_owner",['1st Owner', '2nd Owner','3rd Owner', '4th Owner', '6th Owner'])


input_data=pd.DataFrame({
    'model_year':[model_year],
    'distance_covered':[distance_covered],
    'maker':[maker],
    'fuel_type':[fuel_type],
    'pre_owner':[pre_owner]
})


input_data_encoded=pd.get_dummies(input_data,columns=['maker','fuel_type','pre_owner'])
expected_columns=['model_year', 'distance_covered', 'maker_Audi', 'maker_BMW',
       'maker_Chevrolet', 'maker_Datsun', 'maker_Fiat', 'maker_Ford',
       'maker_Honda', 'maker_Hyundai', 'maker_Jeep', 'maker_KIA', 'maker_MG',
       'maker_Mahindra', 'maker_Maruti', 'maker_Mercedes', 'maker_Nissan',
       'maker_Renault', 'maker_Skoda', 'maker_Ssangyong', 'maker_Tata',
       'maker_Toyota', 'maker_Volkswagen', 'maker_Volvo', 'fuel_type_Diesel',
       'fuel_type_Electric', 'fuel_type_Petrol', 'fuel_type_Petrol + CNG',
       'fuel_type_Petrol + LPG', 'pre_owner_1st Owner', 'pre_owner_2nd Owner',
       'pre_owner_3rd Owner', 'pre_owner_4th Owner', 'pre_owner_6th Owner']

for col in expected_columns:
    if col not in input_data_encoded.columns:
        input_data_encoded[col] = 0

input_data_encoded=input_data_encoded[expected_columns]

if st.button('Predict'):
    prediction=model.predict(input_data_encoded)
    st.write(f'Predicted Car Price:{prediction[0].item():.2f} Rupees')
