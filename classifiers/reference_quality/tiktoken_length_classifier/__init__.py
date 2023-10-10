from pydantic import BaseModel
import tiktoken

INPUT_EXAMPLE = {
    "text": "The sun is shining bright today.",
    "encoding_model": "cl100k_base"
}


class TiktokenLengthClassifierModel(BaseModel):
    text: str
    encding_model: str = "cl100k_base"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def tiktoken_length_classifier(req: TiktokenLengthClassifierModel):
    """Uses the Tiktoken library to count tokens in a string"""
    encoding = tiktoken.get_encoding(req.encoding_model)
    tokens = encoding.encode(req.text)
    num_tokens = len(tokens)

    if num_tokens < 64:
        return {"token_length": "short"}
    elif num_tokens < 256:
        return {"token_length": "medium"}
    else:
        return{"token_length": "long"} 