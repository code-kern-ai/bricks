from pydantic import BaseModel

INPUT_EXAMPLE = {
    "text": """This is the first line.
    And this is the second line.
    Here's a third one, too.
    """,
}

class NewlineSplitterModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def newline_splitter(req: NewlineSplitterModel):
    """Splits a text by newline characters"""
    splits = req.text.split("\n")
    return {"splitted_text" : [val.strip() for val in splits if len(val) > 0]}


