from pydantic import BaseModel

INPUT_EXAMPLE = {
    "text": "https://huggingface.co/sentence-transformers",
}

class NewlineSplitterModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def newline_splitter(req: NewlineSplitterModel):
    """Splits a text by newline characters"""
    splits = req.text.split("\n")
    return {"splitted_text" :[val for val in splits if len(val) > 0]}


