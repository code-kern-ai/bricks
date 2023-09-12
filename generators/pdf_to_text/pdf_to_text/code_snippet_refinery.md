``` python
from PyPDF2 import PdfReader

ATTRIBUTE: str = "link" # only text attributes

def pdf_scanner(record):
    reader = PdfReader(record[ATTRIBUTE].text)
    number_of_pages = len(reader.pages)
    number = 0
    output = ""
    while number < number_of_pages:
        output += "".join(reader.pages[number].extract_text())
        number +=1
    return output
```