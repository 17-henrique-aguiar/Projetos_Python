import streamlit as st
import pandas as pd

st.set_page_config(page_title="Projeto de Análise de Vendas", layout="wide")

st.title("Projeto de Análise de Vendas (Streamlit + Pandas)")
st.write("Faça upload de um arquivo de um arquivo CSV e navegue entre as páginas para anásile.")

# Upload do arquivo
uploaded_file = st.file_uploader("Envie o arquivo CSV", type=["csv"])

# Guardado no Session state para outras páginas acessarem
if uploaded_file:
  st.session_state["df"] = pd.read_csv(uploaded_file)
  st.session_state("Arquivo carregado com sucesso! Acesse as abas laterais.")
else:
  st.warning("Envie um arquivo CSV para começar.")
