from pydantic import BaseModel 
import textstat

class SyllableCountModel(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "This is an english sentence."
            }
        }

def fn_syllable_count(request: SyllableCountModel):
    """Counts the number of sylabbles in a text. 

    Args:
        request (SyllableCountModel): schema of request body

    Returns:
        dict: Syllables of a text
    """
    text = request.text
    syllables = textstat.syllable_count(text)
    return {"time": syllables}

