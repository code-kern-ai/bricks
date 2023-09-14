from pydantic import BaseModel
from PyPDF2 import PdfReader



INPUT_EXAMPLE = {
    "pdf": "",
}


class PdfToTextModel(BaseModel):
    pdf: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def pdf_to_text(req:PdfToTextModel):
    pdf = req.pdf
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)
    number = 0
    output = ""
    while number < number_of_pages:
        output += "".join(reader.pages[number].extract_text())
        number +=1
    return output
