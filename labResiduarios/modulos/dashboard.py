import streamlit as st


def card_modulo(titulo, descricao, status="Ativo"):
    st.markdown(
        f"""
        <div class="card">
            <h3>{titulo}</h3>
            <p>{descricao}</p>
            <b>Status:</b> {status}
        </div>
        """,
        unsafe_allow_html=True,
    )


def mostrar_dashboard():

    st.title("🧪 LabResíduos")

    st.subheader("Sistema Educacional para Ensino de Análises Ambientais")

    st.markdown("""
### Instituto Federal do Rio de Janeiro - IFRJ

**Campus Nilópolis**

**Laboratório CEMMA / CMMA**
""")

    st.divider()

    st.markdown("## 👥 Equipe do Projeto")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("👩‍💻 Desenvolvido por")
        st.write("**Luciana Oliveira de Albuquerque**")

    with col2:
        st.success("👨‍🏫 Professor Responsável")
        st.write("**Renato Ribeiro**")

    with col3:
        st.success("🖥️ Administrador do Sistema")
        st.write("**Raphael Oliveira de Albuquerque**")

    st.divider()

    st.markdown("## 📊 Painel do Sistema")

    a, b, c, d = st.columns(4)

    a.metric("Módulos", "6")
    b.metric("Status", "🟢 Online")
    c.metric("Versão", "2.0")
    d.metric("Plataforma", "Python")

    st.divider()

    st.markdown("## 🧪 Módulos Disponíveis")

    c1, c2, c3 = st.columns(3)

    with c1:
        card_modulo(
            "🧪 Sólidos Totais",
            "Determinação de sólidos totais, fixos e voláteis."
        )

        card_modulo(
            "🧪 Sólidos Suspensos",
            "Determinação de sólidos suspensos."
        )

    with c2:
        card_modulo(
            "🧪 N-Amoniacal",
            "Padronização do ácido sulfúrico."
        )

        card_modulo(
            "🧪 NTK",
            "Nitrogênio Total Kjeldahl."
        )

    with c3:
        card_modulo(
            "🧪 DQO",
            "Demanda Química de Oxigênio."
        )

        card_modulo(
            "🧪 NHX",
            "Mesmo padrão do NTK.",
            "Planejado"
        )

    st.divider()

    st.markdown("## 🚀 Próximas Etapas")

    st.write("✔ Banco de Dados")
    st.write("✔ Exportação para Excel")
    st.write("✔ Relatórios em PDF")
    st.write("✔ Área do Professor")
    st.write("✔ Histórico das Análises")

    st.divider()

    st.info(
        "LabResíduos • Sistema Educacional para Ensino de Análises Ambientais • IFRJ"
    )

    st.caption("Versão 2.0 • Desenvolvido no IFRJ • 2026")
