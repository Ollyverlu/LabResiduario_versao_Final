import sqlite3
from pathlib import Path
from datetime import datetime

# Caminho do banco de dados
CAMINHO_BANCO = Path(__file__).parent.parent / "dados" / "labresiduos.db"


def conectar():
    """
    Conecta ao banco SQLite.
    """
    CAMINHO_BANCO.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(CAMINHO_BANCO)


def criar_tabela():
    """
    Cria a tabela principal caso ainda não exista.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            data_hora TEXT,

            modulo TEXT,

            responsavel TEXT,

            projeto TEXT,

            resultado TEXT,

            observacoes TEXT

        )
    """)

    conn.commit()
    conn.close()


def salvar_resultado(
    modulo,
    responsavel,
    projeto,
    resultado,
    observacoes=""
):
    """
    Salva um resultado no banco.
    """

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO historico(

            data_hora,

            modulo,

            responsavel,

            projeto,

            resultado,

            observacoes

        )

        VALUES (?, ?, ?, ?, ?, ?)

    """, (

        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

        modulo,

        responsavel,

        projeto,

        resultado,

        observacoes

    ))

    conn.commit()
    conn.close()


def listar_resultados():
    """
    Lista todo o histórico.
    """

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT
            id,
            data_hora,
            modulo,
            responsavel,
            projeto,
            resultado,
            observacoes

        FROM historico

        ORDER BY id DESC

    """)

    dados = cursor.fetchall()

    conn.close()

    return dados


def excluir_resultado(id_registro):
    """
    Exclui um registro pelo ID.
    """

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM historico WHERE id=?",
        (id_registro,)
    )

    conn.commit()
    conn.close()


# Cria automaticamente a tabela quando o módulo é importado
criar_tabela()