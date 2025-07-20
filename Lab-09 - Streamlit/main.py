import streamlit as st
import pandas as pd


st.header("Fastfood Nutrition Dataset Analysis")

df = pd.read_csv('input/fastfood.csv')
# st.dataframe(df)
st.dataframe(df.head())
# st.table(df.head())

st.metric(label ="Weekly Revenue", value=499, delta=10, delta_color="normal")
# st.metric(label ="Weekly Revenue", value=499, delta=-10, delta_color="normal")



