import streamlit as st
import pandas as pd
from functions import *

st.set_page_config(layout="wide")

st.title("Officer Details")

# Input fields for UID and Name
col1, col2 = st.columns(2)

with col1:
    uid = st.text_input("Enter Officer UID")

with col2:
    name = st.text_input("Enter Officer Name")

# Button to fetch specific officer data
if st.button("Get Officer Data"):
    if uid:
        officer_data = get_officer_data(uid=uid)
    elif name:
        officer_data = get_officer_data(name=name)
    else:
        officer_data = "Please enter either UID or Name."

    if isinstance(officer_data, str):
        st.error(officer_data)
    elif officer_data:
        st.dataframe(pd.DataFrame(officer_data), use_container_width=True)
    else:
        st.warning("No data found for the provided UID/Name.")

# Button to fetch all officer data
if st.button("Get All Officers"):
    all_officers_data = get_all_officer_data()  # Assuming get_all_officer_data() fetches all officers
    print (all_officers_data)
    print ("Entered frontend")
    if isinstance(all_officers_data, str):
        st.error(all_officers_data)
    elif all_officers_data:
        st.dataframe(pd.DataFrame(all_officers_data), use_container_width=True)
    else:
        st.warning("No officer data found.")

