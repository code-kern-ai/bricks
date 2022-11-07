from pydantic import BaseModel
from typing import Dict
from Levenshtein import distance

INPUT_EXAMPLE = {
    "textFirst": "John Doe",
    "textSecond": "Jon Doe",
    "weights": {"insertion": 1, "deletion": 1, "substitution": 1},
}


class LevenshteinDistanceModel(BaseModel):
    textFirst: str
    textSecond: str
    weights: Dict[str, int] = {
        "insertion": 1,
        "deletion": 1,
        "substitution": 1,
    }

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def levenshtein_distance(request: LevenshteinDistanceModel):
    """Calculates the Levenshtein distance between two strings."""

    text_first = request.textFirst
    text_second = request.textSecond
    weights = request.weights

    if weights is not None:
        weights_tuple = (
            weights["insertion"],
            weights["deletion"],
            weights["substitution"],
        )
        ls_distance = distance(text_first, text_second, weights=weights_tuple)
    else:
        ls_distance = distance(text_first, text_second)
    return {"levenshteinDistance": ls_distance}
