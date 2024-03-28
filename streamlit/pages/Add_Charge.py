import streamlit as st
import pandas as pd
from create_db import set_database
from functions import add_officer, add_charge, existing_officers_name, existing_officers_uid, get_name_rank,get_total_charges,get_name_from_uid,get_name_uid
import numpy as np
st.set_page_config(layout="wide")

st.subheader("Add New Charge")   

col1, col2 = st.columns(2)
officers_to_split = []
officers_amt = []

def add_officer_input():
    print()
    

with col1:
    charge_type = st.selectbox(label="",options=["Split","Individual"])
    if charge_type != "Split":    
        officer_uid = st.selectbox(label="Officer UID",options=["A","B","C"])
    charge_desc = st.text_input(label="Charge Description")
    
    if charge_type == "Split":
        colp, colq, colr = st.columns(3)
        with colq:
            st.text("Current Split")   
        st.dataframe(pd.DataFrame(np.random.randn(5, 2), columns=["Officer Name","Amount"]),use_container_width=True)
        cola, colb = st.columns(2)
        with cola:
            officer_split_id = st.selectbox(label="Officer",options=["A","B","C"])
            officers_to_split.append(officer_split_id)
        with colb:
            officer_split_amt = st.number_input(label="Share")
            officers_amt.append(officer_split_amt)
        
        st.button(label="Add Officer",on_click=add_officer_input())
    charge_amt = st.number_input(label="Total Amount")
    charge_date = st.date_input(label="Date")
    charge_remarks = st.text_input(label="Remarks")
    col_a, col_b, col_c = st.columns(3)
    with col_b:
        st.button(label="Add Charge")
        #st.button(label="Add Charge", on_click=add_charge(officer_uid, charge_desc, charge_amt, charge_date, charge_type))

with col2:
    st.dataframe(pd.DataFrame(np.random.randn(50, 3), columns=("col %d" % i for i in range(3))),use_container_width=True)