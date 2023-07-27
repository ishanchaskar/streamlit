import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.write("hellos")

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

chart = alt.Chart(data).mark_circle().encode(
    x = 'a' , y = 'b', tooltip=['a','b']
)
st.altair_chart(chart , use_container_width=True)

st.map()
#put dataframe inside to mark the values

st.graphviz_chart("""
diagraph{
watch -> like
like -> share
share -> subscribe
share -> watch
} 
""")

plt.scatter(data['a'],data['b'])
plt.title("scatter")
st.pyplot()

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

st.image("wall.jpg")

st.audio("file_example_MP3_700KB.mp3")
st.video("pexels-thirdman-5538262 (1080p).mp4")
#we can paste the yt link too

st.title("widget")
if st.button("subscribe"):
    st.write("like this video")
name = st.text_input("names")
st.write(name)

address =st.text_area("enter your address")
st.write(address)

st.date_input("enter a date")
st.time_input("enter time")
st.checkbox("you accept the T & C" value=True)