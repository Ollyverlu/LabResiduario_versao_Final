import streamlit as st
import numpy as np
from utils.banco import salvar_resultado


def solidos_suspensos():
    st.title("Sólidos Suspensos")

    st.markdown("### Determinação de Sólidos Suspensos, Fixos e Voláteis")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        professor = st.text_input(
            "Professor Responsável",
            value="Renato Ribeiro",
            disabled=True
        )
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
        m1 = st.number_input("m1 - Filtro vazio (g)", value=0.0000, format="%.4f", key="ss_m1")
        m2 = st.number_input("m2 - Após estufa 105°C (g)", value=0.0000, format="%.4f", key="ss_m2")
        m3 = st.number_input("m3 - Após mufla 550°C (g)", value=0.0000, format="%.4f", key="ss_m3")

    with col2:
        st.subheader("Replicata 2")
        m1_2 = st.number_input("m1 - Filtro vazio (g)", value=0.0000, format="%.4f", key="ss_m1_2")
        m2_2 = st.number_input("m2 - Após estufa 105°C (g)", value=0.0000, format="%.4f", key="ss_m2_2")
        m3_2 = st.number_input("m3 - Após mufla 550°C (g)", value=0.0000, format="%.4f", key="ss_m3_2")

    st.divider()

    if st.button("Calcular Sólidos Suspensos"):

        if volume <= 0:
            st.error("Informe um volume válido.")
        else:
            ss1 = ((m2 - m1) * 1_000_000) / volume
            ss2 = ((m2_2 - m1_2) * 1_000_000) / volume

            ssf1 = ((m3 - m1) * 1_000_000) / volume
            ssf2 = ((m3_2 - m1_2) * 1_000_000) / volume

            ssv1 = ss1 - ssf1
            ssv2 = ss2 - ssf2

            media_ss = np.mean([ss1, ss2])
            media_ssf = np.mean([ssf1, ssf2])
            media_ssv = np.mean([ssv1, ssv2])

            desvio_ss = np.std([ss1, ss2], ddof=1)
            desvio_ssf = np.std([ssf1, ssf2], ddof=1)
            desvio_ssv = np.std([ssv1, ssv2], ddof=1)

            st.success("Cálculo realizado com sucesso!")

            c1, c2, c3 = st.columns(3)

            c1.metric("SS", f"{media_ss:.2f} ± {desvio_ss:.2f} mg/L")
            c2.metric("SSF", f"{media_ssf:.2f} ± {desvio_ssf:.2f} mg/L")
            c3.metric("SSV", f"{media_ssv:.2f} ± {desvio_ssv:.2f} mg/L")

            resultado_banco = (
                f"SS = {media_ss:.2f} ± {desvio_ss:.2f} mg/L | "
                f"SSF = {media_ssf:.2f} ± {desvio_ssf:.2f} mg/L | "
                f"SSV = {media_ssv:.2f} ± {desvio_ssv:.2f} mg/L"
            )

            salvar_resultado(
                modulo="Sólidos Suspensos",
                responsavel=aluno,
                projeto=projeto,
                resultado=resultado_banco,
                observacoes="Professor Responsável: Renato Ribeiro"
            )

            st.info("Resultado salvo no banco de dados.")

            st.subheader("Gráfico dos Resultados")

            st.bar_chart({
                "Resultado médio": [media_ss, media_ssf, media_ssv]
            })
