import streamlit as st
import pandas as pd


# App Title
st.title("Widgets in Streamlit")

st.divider()

primary_btn = st.button(label="Run Model", type="primary")
secondary_btn = st.button(label="Secondary", type="secondary")

if primary_btn:
    st.write("Hello World!")


checkbox = st.checkbox("I accept T & C.")

st.divider()

df = pd.read_csv('input/fastfood.csv')
radio = st.radio("Choose Any Dataset Feature", options=df.columns[1:], index=0)
st.divider()
st.write(radio)
st.divider()

select = st.selectbox("Choose Any Dataset Feature", options=df.columns[1:], index=0)
st.divider()
st.write(select)
st.divider()


text_input = st.text_input("Email Address", placeholder="Enter Your Email Address")
st.write(text_input)

st.divider()