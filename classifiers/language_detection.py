from typing import Dict
from langdetect import detect, DetectorFactory 
DetectorFactory.seed = 0

def fn_language_detection(request: Dict):
    """Detect language of text
    
    Args:
        request (Dict): request body

    Returns:
        dict: Language of text
    """

    text = request["text"]
    language = detect(text)
    return {"language": language}
