import html
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "text": """Here&#39;s how &quot;Kern.ai Newsletter&quot; did today. 3. "World&#8217;s largest tech conference: &quot;Innovate 2023&#8482;&quot; begins tomorrow!"""
}

class HtmlUnescapeModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def html_unescape(request: HtmlUnescapeModel):
    """Unescapes HTML entities in a text."""

    text = request.text

    unescaped_text = html.unescape(text)

    return {"Unescaped text": unescaped_text}