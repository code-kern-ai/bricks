```python 
from PyPDF2 import PdfReader

def pdf_scanner(pdf):
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)
    number = 0
    output = ""
    while number < number_of_pages:
        output += "".join(reader.pages[number].extract_text())
        number +=1
    return output


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    pdf = "/mnt/c/Users/svenj/Downloads/XPhoneBERT.pdf"
    print(pdf_scanner(pdf))
example_integration()
```