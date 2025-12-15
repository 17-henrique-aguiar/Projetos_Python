import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title(" Dashboard Final")

if "df" not in st.session_state:
    st.warning("Volte à página inicial e carregue o CSV.")
else:
    df = st.session_state["df"]

    st.subheader("Filtros")
    numeric_cols = df.select_dtypes(include="number").columns

    col_filtro = st.selectbox("Escolha uma coluna numérica para filtrar", numeric_cols)
    min_val = float(df[col_filtro].min())
    max_val = float(df[col_filtro].max())

    filtro = st.slider("intervalo", min_val, max_val, (min_val, max_val))
    df_filtrado = df[(df[col_filtro] >= filtro[0]) & (df[col_filtro] <= filtro[1])]

    st.success(f"{len(df_filtrado)} registros após o filtro")

    st.write("### Dados filtrados")
    st.dataframe(df_filtrado)

    st.write("### KPI - Total")
    st.metric("Soma da coluna filtrada", df_filtrado[col_filtro].sum())

    st.write("### Gráfico")
    fig, ax = plt.subplots()
    ax.plot(df_filtrado[numeric_cols[0]])
    st.pyplot(fig)

    st.write("### Insight autómatico")
    media = df_filtrado[col_filtro].mean()
    maior = df_filtrado[col_filtro].max()
    menor = df_filtrado[col_filtro].min()

    st.info(f"""
        **Insights**
    - Média da coluna filtrada: **{media:.2f}**
    - Valor máximo: **{maior:.2f}**
    - Valor mínimo: **{menor:.2f}**
    """)

    st.download_button(
        "Baixar CSV filtrado",
        df_filtrado.to_csv(index=False),
        file_name="dados_filtrados.csv"    
        )
