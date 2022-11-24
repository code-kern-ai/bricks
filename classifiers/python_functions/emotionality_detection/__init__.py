from pydantic import BaseModel
from LeXmo import LeXmo

INPUT_EXAMPLE = {
    "text": """As Harry went inside the Chamber of Secrets, he discovered the Basilisk's layer. Before him stood Tom
            Riddle, with his wand. Harry was numb for a second as if he had seen a ghost. Moments later the giant 
            snake attacked Harry but fortunately, Harry dodged and ran into one of the sewer lines while the serpent 
            followed. The Basilisk couldn't be killed with bare hands but only with a worthy weapon. After killing the 
            snake with the Gryffindor sword, Harry killed Tom by forging the Basilisk's tooth through his diary where 
            the spirit of Tom resided."""
}


class EmotionalityDetectionModel(BaseModel):
    text: str

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def emotionality_detection(request: EmotionalityDetectionModel):
    """Fetches emotions from a given text"""

    text = request.text
    emo = LeXmo.LeXmo(text)
    emo.pop('text', None)
    emo = max(emo, key=emo.get)

    return {"emotion": emo}
