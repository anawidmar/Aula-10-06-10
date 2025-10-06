import streamlit as st

St tittle("Meu programa")
st.write("Alo mundo")

nome = st.text_input("Digite seu nome:")
if nome:
  st.write(nome.upper())
