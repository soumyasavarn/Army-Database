import streamlit as st
import pandas as pd
import numpy as np

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
        officer_rank = st.text_input(label="Rank")
        subscription_name = st.text_input(label="Subscription Name")
        charge_amt = st.text_input(label="Amount")
        if st.button("Add Subscription"):
            # Add subscription logic here
            pass
    elif st.session_state.mode == "Modify":
        officer_rank1 = st.text_input(label="Rank")
        option = st.selectbox('Subscription Name', ('x', 'y', 'z'))
        charge_amt1 = st.text_input(label="Amount")
        if st.button("Modify Subscription"):
            # Modify subscription logic here
            pass

# Dummy dataframe for demonstration
with col2: 
    data = pd.DataFrame(np.random.randn(50, 3), columns=("col %d" % i for i in range(3)))
    st.dataframe(data, use_container_width=True)
