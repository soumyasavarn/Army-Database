import streamlit as st
import pandas as pd
from functions import *
from pdf import *
st.set_page_config(layout="wide")

st.subheader("Billing")   

col1,col2 = st.columns(2)

with col1:
        officer = st.selectbox("Officer",get_name_uid())
        arrears = st.number_input(label="Arrears")

        if st.button("Generate Bill"):
            st.text(generate_bill(officer,arrears))
            pass
        
