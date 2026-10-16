import streamlit as st

st.set_page_config(
    page_title="Application Dys — Test",
    layout="wide"
)

st.title("Application Dys")
st.success("Streamlit fonctionne.")

st.subheader("Test du stockage local")

try:
    from services.local_storage import prepare_storage
    st.success("Le module de stockage est importé correctement.")

    prepare_storage()

    st.success("Le stockage local est initialisé.")
except Exception as e:
    st.error(f"Erreur de stockage : {e}")
    st.exception(e)
