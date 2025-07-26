import streamlit as st

name = st.text_input("Enter your Name : ")
fname = st.text_input("Enter your Father Name : ")
adr = st.text_area("Enter Your Text : ")
classdata = st.selectbox("Enter Your Class :",(1,2,3,4,5,6,7,8,9,10))

button = st.button("Done")
if button :
    st.markdown(f"""
     Name : {name}
     Father Name : {fname}
     address : {adr}
     class : {classdata}""")


