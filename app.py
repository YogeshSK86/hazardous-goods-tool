import streamlit as st
import pandas as pd
import os

# Load data
df = pd.read_csv('data/hazardous_goods.csv')

# App Title
st.title('Hazardous Goods Movement - Ocean & Air')

# User Input
st.subheader('Enter Your Product Details')
product_name = st.text_input('Product Name')
un_number = st.text_input('UN Number')

if st.button('Search'):
    result = df[(df['Product Name'].str.contains(product_name, case=False, na=False)) | 
                (df['UN Number'].astype(str) == un_number)]
    
    if not result.empty:
        st.success('Hazardous Material Details Found!')
        st.write(result)
        
        # Show Placard if available
        hazard_class = result.iloc[0]['Hazard Class']
        placard_path = f"data/placards/{hazard_class}.png"
        if os.path.exists(placard_path):
            st.image(placard_path, caption=f'Hazard Class: {hazard_class}')
        
    else:
        st.error('No matching hazardous material found.')
