import streamlit as st
import pandas as pd
from create_db import set_database
from functions import add_officer, add_charge, existing_officers_name, existing_officers_uid, get_name_rank,get_total_charges,get_name_from_uid,get_name_uid
import numpy as np
st.set_page_config(layout="wide")

st.subheader("Add New Charge")   

col1, col2 = st.columns(2)

with col1:
    officer_uid = st.text_input(label="Officer UID")
    charge_desc = st.text_input(label="Charge Description")
    charge_amt = st.text_input(label="Amount")
    charge_type = st.selectbox(label="Type",options=[])
    charge_date = st.date_input(label="Date")
    col_a, col_b, col_c = st.columns(3)
    with col_b:
        st.button(label="Add Charge")
        #st.button(label="Add Charge", on_click=add_charge(officer_uid, charge_desc, charge_amt, charge_date, charge_type))

with col2:
    st.dataframe(pd.DataFrame(np.random.randn(50, 3), columns=("col %d" % i for i in range(3))),use_container_width=True)