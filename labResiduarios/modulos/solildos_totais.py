import streamlit as st
import numpy as np
from utils.banco import salvar_resultado

st.write("VERSÃO NOVA DO SÓLIDOS TOTAIS")

def solidos_totais():
    st.title("Sólidos Totais")

    st.markdown("### Determinação de Sólidos Totais, Fixos e Voláteis")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        professor = st.text_input("Professor Responsável", value="Renato Ribeiro", disabled=True)
        aluno = st.text_input("Aluno")

    with col2:
        projeto = st.text_input("Projeto")
        data = st.date_input("Data")
        hora = st.time_input("Hora")

    st.divider()

    volume = st.number_input(
        "Volume da amostra / alíquota (mL)",
        value=50.00,
        format="%.2f"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Replicata 1")
        m1 = st.number_input("m1 - Cápsula vazia (g)", value=0.0000, format="%.4f", key="st_m1")
        m2 = st.number_input("m2 - Após estufa 105°C (g)", value=0.0000, format="%.4f", key="st_m2")
        m3 = st.number_input("m3 - Após mufla 550°C (g)", value=0.0000, format="%.4f", key="st_m3")

    with col2:
        st.subheader("Replicata 2")
        m1_2 = st.number_input("m1 - Cápsula vazia (g)", value=0.0000, format="%.4f", key="st_m1_2")
        m2_2 = st.number_input("m2 - Após estufa 105°C (g)", value=0.0000, format="%.4f", key="st_m2_2")
        m3_2 = st.number_input("m3 - Após mufla 550°C (g)", value=0.0000, format="%.4f", key="st_m3_2")

    st.divider()

    if st.button("Calcular Sólidos Totais"):

        if volume <= 0:
            st.error("Informe um volume válido.")
        else:
            st1 = ((m2 - m1) * 1_000_000) / volume
            st2 = ((m2_2 - m1_2) * 1_000_000) / volume

            stf1 = ((m3 - m1) * 1_000_000) / volume
            stf2 = ((m3_2 - m1_2) * 1_000_000) / volume

            stv1 = st1 - stf1
            stv2 = st2 - stf2

            media_st = np.mean([st1, st2])
            media_stf = np.mean([stf1, stf2])
            media_stv = np.mean([stv1, stv2])

            desvio_st = np.std([st1, st2], ddof=1)
            desvio_stf = np.std([stf1, stf2], ddof=1)
            desvio_stv = np.std([stv1, stv2], ddof=1)

            st.success("Cálculo realizado com sucesso!")

            c1, c2, c3 = st.columns(3)

            c1.metric("ST", f"{media_st:.2f} ± {desvio_st:.2f} mg/L")
            c2.metric("STF", f"{media_stf:.2f} ± {desvio_stf:.2f} mg/L")
            c3.metric("STV", f"{media_stv:.2f} ± {desvio_stv:.2f} mg/L")

            resultado_banco = (
                f"ST = {media_st:.2f} ± {desvio_st:.2f} mg/L | "
                f"STF = {media_stf:.2f} ± {desvio_stf:.2f} mg/L | "
                f"STV = {media_stv:.2f} ± {desvio_stv:.2f} mg/L"
            )

            salvar_resultado(
                modulo="Sólidos Totais",
                responsavel=aluno,
                projeto=projeto,
                resultado=resultado_banco,
                observacoes="Professor Responsável: Renato Ribeiro"
            )

            st.info("Resultado salvo no banco de dados.")

            st.subheader("Gráfico dos Resultados")

            st.bar_chart({
                "Resultado médio": [media_st, media_stf, media_stv]
            })