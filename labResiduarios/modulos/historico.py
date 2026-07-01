import streamlit as st
import pandas as pd
from io import BytesIO
from utils.banco import listar_resultados, excluir_resultado
from utils.pdf import gerar_pdf


def gerar_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Historico")
    return output.getvalue()


def gerar_pdf_bytes(registro):
    output = BytesIO()

    gerar_pdf(
        arquivo=output,
        modulo=registro["Módulo"],
        professor="Renato Ribeiro",
        aluno=registro["Aluno"],
        projeto=registro["Projeto"],
        resultado=registro["Resultado"],
        observacoes=registro["Observações"]
    )

    output.seek(0)
    return output.getvalue()


def historico():
    st.title("Histórico das Análises")

    dados = listar_resultados()

    if not dados:
        st.info("Ainda não há resultados salvos.")
        return

    df = pd.DataFrame(
        dados,
        columns=[
            "ID",
            "Data/Hora",
            "Módulo",
            "Aluno",
            "Projeto",
            "Resultado",
            "Observações"
        ]
    )

    st.subheader("Filtros")

    col1, col2, col3 = st.columns(3)

    with col1:
        filtro_aluno = st.text_input("Pesquisar por aluno")

    with col2:
        filtro_projeto = st.text_input("Pesquisar por projeto")

    with col3:
        filtro_modulo = st.selectbox(
            "Filtrar por módulo",
            ["Todos"] + sorted(df["Módulo"].dropna().unique().tolist())
        )

    df_filtrado = df.copy()

    if filtro_aluno:
        df_filtrado = df_filtrado[
            df_filtrado["Aluno"].str.contains(filtro_aluno, case=False, na=False)
        ]

    if filtro_projeto:
        df_filtrado = df_filtrado[
            df_filtrado["Projeto"].str.contains(filtro_projeto, case=False, na=False)
        ]

    if filtro_modulo != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Módulo"] == filtro_modulo]

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric("Total de registros", len(df_filtrado))
    c2.metric("Módulos diferentes", df_filtrado["Módulo"].nunique())
    c3.metric("Alunos diferentes", df_filtrado["Aluno"].nunique())

    st.divider()

    st.subheader("Tabela de Resultados")
    st.dataframe(df_filtrado, use_container_width=True)

    st.divider()

    st.subheader("Exportar Histórico em Excel")

    excel_bytes = gerar_excel(df_filtrado)

    st.download_button(
        label="Baixar Histórico em Excel",
        data=excel_bytes,
        file_name="historico_labresiduos.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.divider()

    st.subheader("Gerar PDF de um Registro")

    id_pdf = st.number_input(
        "Digite o ID do registro para gerar PDF",
        min_value=0,
        step=1
    )

    if id_pdf > 0:
        registro_pdf = df[df["ID"] == id_pdf]

        if registro_pdf.empty:
            st.warning("ID não encontrado.")
        else:
            registro = registro_pdf.iloc[0]
            pdf_bytes = gerar_pdf_bytes(registro)

            st.download_button(
                label="Baixar PDF do Registro",
                data=pdf_bytes,
                file_name=f"registro_{id_pdf}_labresiduos.pdf",
                mime="application/pdf"
            )

    st.divider()

    st.subheader("Excluir Registro")

    id_excluir = st.number_input(
        "Digite o ID do registro que deseja excluir",
        min_value=0,
        step=1,
        key="excluir_id"
    )

    if st.button("Excluir registro selecionado"):
        if id_excluir <= 0:
            st.warning("Informe um ID válido.")
        else:
            excluir_resultado(id_excluir)
            st.success("Registro excluído com sucesso. Atualize a página.")