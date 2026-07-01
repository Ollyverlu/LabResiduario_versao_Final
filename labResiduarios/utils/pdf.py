from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.units import cm


def gerar_pdf(
    arquivo,
    modulo,
    professor,
    aluno,
    projeto,
    resultado,
    observacoes=""
):

    doc = SimpleDocTemplate(arquivo)

    styles = getSampleStyleSheet()

    elementos = []

    elementos.append(
        Paragraph("<b>LABRESÍDUOS</b>", styles["Title"])
    )

    elementos.append(
        Paragraph(
            "Sistema Educacional para Ensino de Análises Ambientais",
            styles["Heading2"]
        )
    )

    elementos.append(Spacer(1, 0.5 * cm))

    elementos.append(
        Paragraph(
            "<b>Instituto Federal do Rio de Janeiro - IFRJ</b>",
            styles["Heading3"]
        )
    )

    elementos.append(
        Paragraph(
            "Campus Nilópolis",
            styles["Normal"]
        )
    )

    elementos.append(
        Paragraph(
            "Laboratório CEMMA / CMMA",
            styles["Normal"]
        )
    )

    elementos.append(Spacer(1, 0.6 * cm))

    tabela = Table([

        ["Professor Responsável", professor],

        ["Aluno", aluno],

        ["Projeto", projeto],

        ["Módulo", modulo]

    ])

    tabela.setStyle(

        TableStyle([

            ("BACKGROUND", (0, 0), (0, -1), colors.lightgreen),

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold")

        ])

    )

    elementos.append(tabela)

    elementos.append(Spacer(1, 0.7 * cm))

    elementos.append(
        Paragraph("<b>RESULTADOS</b>", styles["Heading2"])
    )

    elementos.append(
        Paragraph(resultado, styles["Normal"])
    )

    elementos.append(Spacer(1, 0.5 * cm))

    elementos.append(
        Paragraph("<b>Observações</b>", styles["Heading2"])
    )

    elementos.append(
        Paragraph(observacoes, styles["Normal"])
    )

    elementos.append(Spacer(1, 1 * cm))

    elementos.append(
        Paragraph(
            "Professor Responsável: Renato Ribeiro",
            styles["Normal"]
        )
    )

    elementos.append(
        Paragraph(
            "Desenvolvido por Luciana Oliveira de Albuquerque",
            styles["Normal"]
        )
    )

    elementos.append(
        Paragraph(
            "LabResíduos • Versão 2.0 • IFRJ • 2026",
            styles["Normal"]
        )
    )

    doc.build(elementos)