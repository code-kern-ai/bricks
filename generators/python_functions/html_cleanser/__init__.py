from pydantic import BaseModel
from typing import Optional, List
from bs4 import BeautifulSoup

INPUT_EXAMPLE = {
    "html": """
            <!DOCTYPE html>
            <html>
            <body>
            <h1>Website header</h1>
            <p>
            Hello world.
            My website is live!
            </p>
            </body>
            </html>
            """
}

class HtmlCleanserModel(BaseModel):
    html: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def html_cleanser(req: HtmlCleanserModel):
    '''Removes the HTML tags from a text.'''
    html = req.html

    soup = BeautifulSoup(html, "html.parser")

    # Remove any line breakers as well
    text = soup.text.splitlines()
    text = " ".join([w for w in text if len(w) >= 1])

    return {"Cleaned text": text}


