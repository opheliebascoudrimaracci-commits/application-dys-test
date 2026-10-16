import streamlit as st

st.set_page_config(
    page_title="Application Dys — Test",
    layout="wide"
)

st.title("Application Dys")
st.success("Le démarrage de Streamlit fonctionne.")

if st.button("Ouvrir les modules"):
    st.info("Test de navigation réussi.")
