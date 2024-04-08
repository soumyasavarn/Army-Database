import streamlit as st
from functions import *
from pdf import *
from datetime import datetime
st.set_page_config(layout="wide")

st.subheader("Billing")   

col1,col2 = st.columns(2)

with col1:
        officer = st.selectbox("Officer",get_name_uid())
        # select_month = st.selectbox("Month",mon)
        from calendar import month_abbr
        from datetime import datetime

        with st.expander('Billing Month'):
            this_year = datetime.now().year
            this_month = datetime.now().month
            report_year = st.selectbox("", range(this_year, this_year - 5, -1))
            month_abbr = month_abbr[1:]
            report_month_str = st.radio("", month_abbr, index=this_month - 1, horizontal=True)
            report_month = month_abbr.index(report_month_str) + 1

        arrears = st.number_input(label="Arrears")
        
        if st.button("Generate Bill"):
            st.text(generate_bill(officer,arrears,report_month_str,report_year))
            pass

       
        
        
