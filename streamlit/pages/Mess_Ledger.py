import streamlit as st
import pandas as pd
from create_db import set_database
from functions import *
st.set_page_config(layout="wide")

st.subheader("Add New Entry")   

col1, col2 = st.columns(2)

with col1:
    officer_uid=""
    mess_type = st.selectbox(label="Charge Type",options=["Normal","Daily Messing","Extra Messing"])
    
    mess_desc = st.text_input(label="Description")
    mess_remarks = st.text_input(label="Remarks")
    mess_amt = st.number_input(label="Amount")
    if mess_type != "Normal":
        officer_uid = st.selectbox(label="Officer Associated",options=get_name_uid_mess_member())
    charge_date = st.date_input(label="Date")
    col_a, col_b, col_c = st.columns(3)
    with col_b:
        if st.button(label="Add"):
            st.text(add_mess_entry(mess_type, mess_desc, mess_remarks, mess_amt, officer_uid, charge_date))
        

with col2:
    mess_entries = get_mess_entry()
    st.dataframe(pd.DataFrame(mess_entries,columns=["Type", "Description", "Amount"]),use_container_width=True)