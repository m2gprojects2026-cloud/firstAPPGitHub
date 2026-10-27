import streamlit as st
import google.generativeai as genai
genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)
if st.button("Probar"):
    r = model.generate_content(
        "Dime qué es un cambio de aceite."
    )
    st.write(r.text)
