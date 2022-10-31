from pydantic import BaseModel 
import textstat

class ReadingTimeModel(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "This is an english sentence."
            }
        }

def fn_reading_time(request: ReadingTimeModel):
    """Calculate the reading time of a text.
    Based on following paper: https://homepages.inf.ed.ac.uk/keller/papers/cognition08a.pdf
    
    Args:
        reequest (ReadingTimeModel): schema of request body

    Returns:
        dict: Reading time of a text
    """
    text = request.text
    time_to_read = textstat.reading_time(text, ms_per_char=14.69)
    return {"time": time_to_read}

