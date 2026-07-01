
import streamlit as st
from pathlib import Path

from modulos.dashboard import mostrar_dashboard
from modulos.solidos_totais import solidos_totais
from modulos.solidos_suspensos import solidos_suspensos
from modulos.N_Amoniacal import n_amoniacal
from modulos.ntk import ntk
from modulos.dqo import dqo
from modulos.historico import historico
from modulos.sobre import sobre


st.set_page_config(
    page_title="LabResíduos - IFRJ",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)


def carregar_css():
    css = Path(__file__).parent / "assets" / "style.css"

    if css.exists():
        with open(css, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    else:
        st.warning(f"Arquivo CSS não encontrado: {css}")


carregar_css()


st.sidebar.title("🧪 LabResíduos")

menu = st.sidebar.radio(
    "Sistema Educacional",
    [
        "Dashboard",
        "Sólidos Totais",
        "Sólidos Suspensos",
        "N-Amoniacal",
        "NTK",
        "DQO",
        "Histórico",
        "Sobre"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Equipe")

st.sidebar.write("👩‍💻 **Desenvolvido por**")
st.sidebar.write("Luciana Oliveira de Albuquerque")

st.sidebar.write("👨‍🏫 **Professor Responsável**")
st.sidebar.write("Renato Ribeiro")

st.sidebar.write("🖥️ **Administrador do Sistema**")
st.sidebar.write("Raphael Oliveira de Albuquerque")

st.sidebar.markdown("---")
st.sidebar.success("Versão 1.0")


if menu == "Dashboard":
    mostrar_dashboard()

elif menu == "Sólidos Totais":
    solidos_totais()

elif menu == "Sólidos Suspensos":
    solidos_suspensos()

elif menu == "N-Amoniacal":
    n_amoniacal()

elif menu == "NTK":
    ntk()

elif menu == "DQO":
    dqo()

elif menu == "Histórico":
    historico()

elif menu == "Sobre":
    sobre()


st.markdown("---")

st.caption(
    "LabResíduos • Sistema Educacional para Ensino de Análises Ambientais • "
    "Instituto Federal do Rio de Janeiro (IFRJ) • Campus Nilópolis • "
    "Laboratório CEMMA / CMMA"
)