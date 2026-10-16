import streamlit as st
import traceback

st.set_page_config(
    page_title="Application Dys — Diagnostic",
    layout="wide"
)

st.title("Application Dys")
st.success("Streamlit fonctionne.")

st.subheader("Test du programme principal")

try:
    import application_mathis
    st.success("Le programme principal a terminé son chargement.")
except Exception:
    st.error("Une erreur est survenue dans application_mathis.py")
    st.code(traceback.format_exc())
