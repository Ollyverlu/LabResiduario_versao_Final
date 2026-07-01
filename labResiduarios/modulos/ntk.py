
import streamlit as st
import numpy as np
from utils.banco import salvar_resultado


def ntk():
    st.title("NTK")

    st.markdown("### Determinação de Nitrogênio Total Kjeldahl")
    st.markdown("### Padronização do Ácido Sulfúrico 0,02 eqg/L")
    st.markdown("**Padrão primário:** Tetraborato de Sódio Deca Hidratado")
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
        data = st.date_input("Data da análise")
        hora = st.time_input("Hora da análise")

    st.divider()

    st.subheader("Dados Gerais")

    massa_pesada = st.number_input(
        "Massa pesada (g)",
        value=0.0000,
        format="%.4f"
    )

    massa_molar = 381.40

    volume_balao = st.number_input(
        "Volume do balão volumétrico (mL)",
        value=1000.00,
        format="%.2f"
    )

    volume_aliquota = st.number_input(
        "Volume da alíquota (mL)",
        value=10.00,
        format="%.2f"
    )

    st.info(f"Massa molar: {massa_molar:.2f} g/mol")

    st.divider()

    st.subheader("Titulações")

    conc_teorica = 0.02

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 1ª Titulação")
        v1 = st.number_input(
            "Volume de H2SO4 gasto 1 (mL)",
            value=0.0000,
            format="%.4f",
            key="ntk_v1"
        )

    with col2:
        st.markdown("### 2ª Titulação")
        v2 = st.number_input(
            "Volume de H2SO4 gasto 2 (mL)",
            value=0.0000,
            format="%.4f",
            key="ntk_v2"
        )

    with col3:
        st.markdown("### 3ª Titulação")
        v3 = st.number_input(
            "Volume de H2SO4 gasto 3 (mL)",
            value=0.0000,
            format="%.4f",
            key="ntk_v3"
        )

    st.divider()

    if st.button("Calcular NTK"):

        if volume_aliquota <= 0:
            st.error("Informe um volume de alíquota válido.")
        else:
            conc_real_1 = (v1 / volume_aliquota) * conc_teorica
            conc_real_2 = (v2 / volume_aliquota) * conc_teorica
            conc_real_3 = (v3 / volume_aliquota) * conc_teorica

            valores = [conc_real_1, conc_real_2, conc_real_3]

            media = np.mean(valores)
            desvio = np.std(valores, ddof=1)

            dpr = (desvio / media) * 100 if media != 0 else 0
            fator_correcao = conc_teorica / media if media != 0 else 0

            st.success("Cálculo realizado com sucesso!")

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Concentração real", f"{media:.6f} eqg/L")
            c2.metric("Concentração teórica", f"{conc_teorica:.2f} eqg/L")
            c3.metric("DPR", f"{dpr:.2f} %")
            c4.metric("Fator", f"{fator_correcao:.6f}")

            resultado_banco = (
                f"Concentração real = {media:.6f} eqg/L | "
                f"DPR = {dpr:.2f}% | "
                f"Fator = {fator_correcao:.6f}"
            )

            salvar_resultado(
                modulo="NTK",
                responsavel=aluno,
                projeto=projeto,
                resultado=resultado_banco,
                observacoes="Professor Responsável: Renato Ribeiro"
            )

            st.info("Resultado salvo no banco de dados.")

            st.subheader("Resultados por titulação")

            st.write(f"1ª titulação: {conc_real_1:.6f} eqg/L")
            st.write(f"2ª titulação: {conc_real_2:.6f} eqg/L")
            st.write(f"3ª titulação: {conc_real_3:.6f} eqg/L")
            st.write(f"Desvio padrão: {desvio:.6f}")

            st.subheader("Gráfico das concentrações reais")

            st.bar_chart({
                "Concentração real": [conc_real_1, conc_real_2, conc_real_3]
            })