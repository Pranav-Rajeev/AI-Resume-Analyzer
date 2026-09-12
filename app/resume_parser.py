import fitz


def extract_text_from_pdf(data):
    text = ""

    pdf = fitz.open(
        stream=data,
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text