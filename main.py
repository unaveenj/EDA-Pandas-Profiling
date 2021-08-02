import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import time
from streamlit_pandas_profiling import st_profile_report
import numpy as np

#Title
st.title("EDA Analysis App")
st.write("Drag and drop your dataset for quicker EDA analysis")

#Uploader
upload = st.sidebar.file_uploader(label="⏫ Upload your file here ⏫",type=['csv'])

if upload is not None:
    @st.cache
    def load_csv(upload):
        df=pd.read_csv(upload)
        return df

    df = load_csv(upload)
    report = ProfileReport(df,explorative=True)
    st.header("Inputted DataFrame")
    st.write(df)
    with st.spinner('Preparing EDA for your DataFrame'):
        time.sleep(5)
    st.success('Done!')
    st.balloons()
    st.header('**Pandas Profiling Report**')
    st_profile_report(report)

else:
    st.sidebar.info("Upload a CSV file for EDA report")

