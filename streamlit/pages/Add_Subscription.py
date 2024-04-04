import streamlit as st
import pandas as pd
import numpy as np
from functions import *
st.set_page_config(layout="wide")

st.subheader("Add/Modify Subscription")   



# Initialize mode using session state
if 'mode' not in st.session_state:
    st.session_state.mode = "Modify"  # Default mode is "Modify"

# with col1:
c1, c2,c3 ,c4 = st.columns(4)
with c2:
    if st.button("Add"):
        st.session_state.mode = "Add"  # Set mode to "Add" if Add button is clicked
with c1:
    if st.button("Modify"):
        st.session_state.mode = "Modify"  # Set mode to "Modify" if Modify button is clicked
col1, col2 = st.columns(2)
# Render input fields based on mode
with col1:
    if st.session_state.mode == "Add":
        rank_1 = st.checkbox("Rank 1")
        rank_2 = st.checkbox("Rank 2")
        rank_3 = st.checkbox("Rank 3")
        rank_4 = st.checkbox("Rank 4")
        subscription_name = st.text_input(label="Subscription Name")
        charge_amt = st.text_input(label="Amount")
        if st.button("Add Subscription"):
            rank_applicable=[rank_1,rank_2,rank_3,rank_4]
            print(rank_applicable)
            st.text(addto_fixed_charges(rank_applicable, subscription_name,charge_amt))
            pass
    elif st.session_state.mode == "Modify":
        rank = st.selectbox('Rank', ["Rank 1","Rank 2","Rank 3","Rank 4"])
        name_option = st.selectbox('Subscription Name', get_fixed_charges_name())
        charge_amt1 = st.text_input(label="Amount")
        if st.button("Modify Subscription"):
            st.text(modify_fixed_charge(name_option,rank,charge_amt1))
            pass

# Dummy dataframe for demonstration
with col2: 
    fixed_charge_list = get_fixed_charges()
    st.dataframe(pd.DataFrame(fixed_charge_list,columns=["Fixed Charge","Rank 1", "Rank 2","Rank 3","Rank 4"]),use_container_width=True)
