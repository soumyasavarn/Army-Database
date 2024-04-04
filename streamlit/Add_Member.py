import streamlit as st
import pandas as pd
from create_db import set_database
from functions import *
import numpy as np
st.set_page_config(layout="wide")

set_database()

st.subheader("Add New Member")   

col1, col2 = st.columns(2)

with col1:
    
    officer_uid = ""
    officer_rank = ""
    officer_unit = ""
    married = False
    accomadation = False
    mess_member = False
    
    guest = st.toggle('Guest')
    officer_name = st.text_input(label="Name")
    if not (guest):
        officer_uid = st.text_input(label="UID")
        officer_rank = st.selectbox(label="Rank",options=["Rank 1","Rank 2","Rank 3","Rank 4"])
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
        if st.button(label="Add Member"):
            st.text(add_officer(officer_uid, officer_name, officer_rank, officer_unit, married, accomadation, mess_member, guest))
            

with col2:
    name_and_rank = get_name_rank()
    st.dataframe(pd.DataFrame(name_and_rank, columns = ["Name","Rank"]),use_container_width=True)
    print(name_and_rank)

