"""Point d’entrée Application Dys."""
import streamlit as st
st.set_page_config(page_title="Application Dys", page_icon="💜", layout="wide")
try:
    import application_mathis
except Exception:
    import traceback
    st.error("Erreur au démarrage d’Application Dys")
    st.code(traceback.format_exc())
