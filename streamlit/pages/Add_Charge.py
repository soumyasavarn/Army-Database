import streamlit as st
import pandas as pd
from create_db import set_database
from functions import *
import numpy as np
st.set_page_config(layout="wide")

st.subheader("Add New Charge")   

col1, col2 = st.columns(2)  




with col1:
    officers_split = []
    charge_type = st.selectbox(label="",options=["Split","Individual"])
    if charge_type != "Split":    
        officer_uid = st.selectbox(label="Officer UID",options=["A","B","C"])
    charge_desc = st.text_input(label="Charge Description")
    
    if charge_type == "Split":
        officers_split = get_current_split()
        print(officers_split)
        if (len(officers_split)==None):
            st.text("Add Officers to split")
        else:
            colp, colq, colr = st.columns(3)
            with colq:
                st.text("Current Split")       
            st.dataframe(pd.DataFrame(officers_split,columns=["Name","Share"]),use_container_width=True)
        cola, colb = st.columns(2)
        with cola:
            officer_split_id = st.selectbox(label="Officer",options=["A","B","C"])
            
        with colb:
            officer_split_amt = st.number_input(label="Share")
        if st.button(label="Add Officer"):
            st.text(addto_current_split(officer_split_id, officer_split_amt))
        
        
        
    charge_amt = st.number_input(label="Total Amount")
    charge_date = st.date_input(label="Date")
    charge_remarks = st.text_input(label="Remarks")
    col_a, col_b, col_c = st.columns(3)
    with col_b:
        if st.button(label="Add Charge"):
            st.text(add_charge(charge_type, officer_uid, charge_desc, charge_amt, charge_date, charge_remarks, officers_split))
        

with col2:
    charge_list = get_charges()
    st.dataframe(pd.DataFrame(charge_list,columns=["UID","Description", "Amount","Date"]),use_container_width=True)