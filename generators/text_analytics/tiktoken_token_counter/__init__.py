from pydantic import BaseModel
import tiktoken

INPUT_EXAMPLE = {
    "text": "What a beautiful day to count tokens."
}


class TiktokenTokenCounterModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def tiktoken_token_counter(req: TiktokenTokenCounterModel):
    """Uses the Tiktoken library to count tokens in a string"""
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(req.text)
    return {"token_length": len(tokens)}