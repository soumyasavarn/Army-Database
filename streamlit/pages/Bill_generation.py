import streamlit as st
from functions import *
from pdf import *
from datetime import datetime
st.set_page_config(layout="wide")

st.subheader("Billing")   

col1,col2 = st.columns(2)

with col1:
        officer = st.selectbox("Officer",get_name_uid())
        arrears = st.number_input(label="Arrears")
        mon=[ "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]
        select_month = st.selectbox("Month",mon)

       
        if st.button("Generate Bill"):
            st.text(generate_bill(officer,arrears,select_month))
            pass
        
