import streamlit as st
st.title("hello")
st.header("header")
st.subheader("subheader")
st.text("this is a normal text section")
st.markdown("""  this is a markdown example 
     # h1 tag
     ## h3 tag
     :moon:<br>
     :sunglasses:     
     <b>bold</b>
     <i> italics </i>
     """, True)
st.latex(r''' a + ar ''')
st.write(" # ishan")
st.write(st)
#instead of st ( module ) if we put the function we will get the documentation of the function
