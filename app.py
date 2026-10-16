import streamlit as st
import importlib.util

st.set_page_config(
    page_title="Application Dys — Test des modules",
    layout="wide"
)

st.title("Application Dys")
st.sidebar.title("Menu principal")

modules = {
    "Accueil": "accueil.py",
    "Lecture": "lecture.py",
    "Dictée": "dictee.py",
    "Grammaire": "grammaire.py",
    "Histoires": "histoires.py",
    "Entraînement": "entrainement.py",
}

choix = st.sidebar.radio("Choisir un onglet", list(modules))

fichier = modules[choix]

if importlib.util.find_spec(fichier.replace(".py", "")):
    st.success(f"Le module {choix} est accessible.")
else:
    st.error(f"Le fichier {fichier} est introuvable.")
