import streamlit as st
import pandas as pd

st.title("Limpeza de Dados")

if "df" not in st.session_state:
    st.warning("Volte à página inicial e carregue o CSV.")
else:
    df = st.session_state["df"]
    st.write("### Dados Brutos")
    st.dataframe(df)

    st.write("### Informações Gerais")
    st.write(df.info())

    st.write("### Remover valores nulos")
    if st.button("Remover linhas nulas"):
        df = df.dropna()
        st.session_state["df"] = df
        st.success("Linhas nulas removidas")

    st.write("### Remover duplicados")
    if st.button("Remover duplicados"):
        df = df.drop_duplicates()
        st.session_state["df"] = df
        st.success("Duplicados removidos!")

    st.write("### Converter colunas numéricas")
    col = st.selectbox("Escolha a coluna:", df.columns)
    if st.button("Converter para número"):
        df[col] = pd.to_numeric(df[col], errors="coerce")
        st.session_state["df"] = df
        st.success("Coluna convertida!")