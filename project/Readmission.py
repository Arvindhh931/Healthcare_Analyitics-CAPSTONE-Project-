import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64

st.set_page_config(page_title='Hospital Readmission',page_icon="🚑")
st.header("Predict the hospital Re-admission")

selected = option_menu(menu_title=None,options=["Prediction","Project","Information"],
icons=["house","book","envelope"],menu_icon="cast",default_index=0,
orientation='horizontal',
styles={
            "container": {"padding": "0!important", "background-color": "#000"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#000"},
            "nav-link-selected": {"background-color": "green"},
        })
if selected == "Prediction":
    st.markdown("### This is Prediction")
    Age = st.slider("Age",0,120,1,)
    confirm = st.button("Submit")
    if confirm:
        st.success(f"Your age is {Age}")

    







