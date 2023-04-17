from pydantic import BaseModel
import textstat

INPUT_EXAMPLE = {"text": "This sentence should take less than 1 second to read."}


class ReadingTimeModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def reading_time(request: ReadingTimeModel):
    """Calculate the reading time of a text."""
    text = request.text
    time_to_read = textstat.reading_time(text, ms_per_char=14.69)
    return {"readingTime": time_to_read}
