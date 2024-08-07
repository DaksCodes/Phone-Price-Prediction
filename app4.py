import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Load the model
with open(r'C:\Users\adaks\AppData\Local\Programs\Python\Python312\Scripts\Phone Price Prediction\DecisionTreeModelPhone.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the dataset to extract options
data = pd.read_csv(r'C:\Users\adaks\AppData\Local\Programs\Python\Python312\Scripts\Phone Price Prediction\Phone_cleaned_dataset.csv')
# Extract unique brands
brands = data['Brand me'].unique()

def main():
    #styling is also applied to make it text aligned as centre
    st.markdown("<h1 style='text-align: center;'>Phone Price Prediction</h1>", unsafe_allow_html=True)

    # Select Brand
    Brand = st.selectbox('Brand', ['Select Your Brand'] + list(brands))

    # Select RAM, Size, etc., based on filtered options
    RAM = st.selectbox('RAM (in GB)', ['Select Your Desired RAM'] + [4,6,8,10,12,16])

    mob_size = st.slider(
        'Size of Mobile (in inches)',
        min_value=4.7,   # Minimum value
        max_value=7.0, # Maximum value
        value=5.85,      # Default value
        step=0.1         # Step size
    )
    
    primary_cam = st.slider(
        'Primary Camera (in Mega Pixels)',
        min_value=10,   # Minimum value
        max_value=200, # Maximum value
        value=104,      # Default value
        step=10         # Step size
    )
    selfie_cam = st.slider(
        'Selfie Camera (in Mega Pixels)',
        min_value=2,   # Minimum value
        max_value=40, # Maximum value
        value=21,      # Default value
        step=1        # Step size
    )
    battery_pow = st.slider(
        'Battery Power (in mAh)',
        min_value=1500,   # Minimum value
        max_value=6000, # Maximum value
        value=3750,      # Default value
        step=100         # Step size
    )
    # Check if all selections are made
    if (Brand == 'Select Your Brand' or RAM=='Select Your Desired RAM'):
        st.warning('Please select values for all attributes.')
        return
    
    input_df = pd.DataFrame([[Brand, RAM, mob_size, primary_cam, selfie_cam, battery_pow]],
                            columns=['Brand me', 'RAM', 'Mobile_Size', 'Primary_Cam', 'Selfi_Cam', 'Battery_Power'])

    if st.button('Predict'):
        prediction = model.predict(input_df)
        output = round(prediction[0], 2)
        #string s;
        if(output>5000.00):
            s="Mid Range phone"
        elif(output>7000.00):
            s="FlagPost phone"
        elif(output>10000.00):
            s="Premium phone"
        else:
            s="Entry Level phone"
        st.success("The phone would cost you approximately INR {} The phone is a {} quality phone".format(output,s))

if __name__ == '__main__':
    main()
