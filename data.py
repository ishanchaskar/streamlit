import streamlit as st
import pandas as pd
import numpy as np
import time 
a = [1,2,4,5,6,7]
n = np.array(a)
#nd = n.reshape((2,4))
dic = {
    "name":"ishan",
    "Age":20,
    "city":"coimbatore"
} 
data = pd.read_csv('Student_marks.csv')
st.dataframe(data, width=200,height=300)
st.table(dic)
st.json(dic)
st.write(data)
@st.cache_data

def ref_time():
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ref_time())

if st.checkbox("2"):
    st.write(ref_time())

    
    