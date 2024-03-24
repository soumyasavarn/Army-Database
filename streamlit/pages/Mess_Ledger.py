import streamlit as st
import pandas as pd
from create_db import set_database
from functions import add_officer, add_charge, existing_officers_name, existing_officers_uid, get_name_rank,get_total_charges,get_name_from_uid,get_name_uid
import numpy as np
st.set_page_config(layout="wide")

st.subheader("Add New Entry")   

col1, col2 = st.columns(2)

with col1:
    mess_desc = st.text_input(label="Description")
    mess_amt = st.text_input(label="Amount")
    mess_type = st.selectbox(label="type",options=["Credit","Debit"])
    mess_officer = st.text_input(label="Officer Associated")
    charge_date = st.date_input(label="Date")
    col_a, col_b, col_c = st.columns(3)
    with col_b:
        st.button(label="Add")

with col2:
    st.dataframe(pd.DataFrame(np.random.randn(50, 3), columns=("col %d" % i for i in range(3))),use_container_width=True)