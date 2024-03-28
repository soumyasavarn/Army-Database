import streamlit as st
import pandas as pd
from create_db import set_database
from functions import add_officer, add_charge, existing_officers_name, existing_officers_uid, get_name_rank,get_total_charges,get_name_from_uid,get_name_uid
import numpy as np
st.set_page_config(layout="wide")

def refresh_officers(dataframe):
    officers_data = get_name_rank()  # Fetch officers' details from the database
    print(type(officers_data))
    officers_df = pd.DataFrame(officers_data)
    print(officers_df)
    dataframe.update(data=officers_df)

def refresh_charges(dataframe):
    charges_data = get_name_rank()  # Fetch charges' details from the database
    dataframe.update(data=charges_data)

set_database()
print(get_name_rank)

st.subheader("Add New Member")   

col1, col2 = st.columns(2)

with col1:    
    guest = st.toggle('Guest')
    officer_name = st.text_input(label="Name")
    if not (guest):
        officer_uid = st.text_input(label="UID")
        officer_rank = st.selectbox(label="Rank",options=["Rank 1","Rank 2","Rank 3"])
        officer_unit = st.text_input(label="Unit")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            married = st.checkbox(label = "Married")
        with col_b:
            accomadation = st.checkbox(label = "Accomadation")
        with col_c:
            mess_member = st.checkbox(label = "Mess Member")
    col_a, col_b, col_c = st.columns(3)
    with col_b:
        st.button(label="Add Member")
        #st.button(label="Add Member",on_click=add_officer(officer_uid, officer_name, officer_rank, officer_unit))

with col2:
    st.dataframe(pd.DataFrame(np.random.randn(50, 3), columns=("col %d" % i for i in range(3))),use_container_width=True)

#print (get_total_charges(12))
#print (get_name_from_uid(12))
