# importere bibliotek
import os
import streamlit as st

from langchain_ollama import ChatOllama
from langchain.embeddings import HuggingFaceEmbeddings

# Working dir.
working_dir = os.path.dirname(os.path.abspath(__file__))

# Sidekonfigurasjon
st.set_page_config(
    page_title="Dokumentsnakk",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Dokumentsnakk")
st.markdown("Ein enkel app for å snakka med pdf-dokument. Lokale modellar med Ollama")

# Laste opp pdf-fil
st.markdown("### Last opp pdf-fil")
opplasta_fil = st.file_uploader("Velg ei fil", type=["pdf"])
filnamn = opplasta_fil.name


# Brukarspørsmål
spørsmål = st.text_input("Kva lurer du på?")




#### Kode for å snakka med pdf-dokument

llm = ChatOllama(
    model="gemma2:2B",
    temperature=0
)

embeddings = HuggingFaceEmbeddings()

def få_svar(filnamn, spørsmål):
    fil_sti = f"{working_dir}/{filnamn}"
    