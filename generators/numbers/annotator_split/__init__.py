from pydantic import BaseModel
import random

INPUT_EXAMPLE = {
    "number": 4
}


class AnnotationSplitModel(BaseModel):
    number: int

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}

def annotator_split(request: AnnotationSplitModel):
    """Generates a random number for split annotation"""
    number = request.number
    return random.randint(0, number-1)
