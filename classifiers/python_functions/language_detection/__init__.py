from pydantic import BaseModel
from langdetect import detect, DetectorFactory 
DetectorFactory.seed = 0

class LanguageDetectionModel(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "This is an english sentence."
            }
        }


def fn_language_detection(request: LanguageDetectionModel):
    """Detect language of text
        
    Args:
        request (LanguageDetectionModel): schema of request body

    Returns:
        dict: Language of text
    """

    text = request.text
    language = detect(text)
    return {"language": language}

