from pydantic import BaseModel
from flashtext import KeywordProcessor
from typing import List

INPUT_EXAMPLE = {
    "text": "I had such an amazing time in the movies. The popcorn was delicious as well.",
    "keywords": ["movies", "popcorn"],
}


class KeywordExtractionModel(BaseModel):
    text: str
    keywords: List[str]

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def keyword_extraction(request: KeywordExtractionModel):
    """Extracts key phrases in a body of text"""

    text = request.text
    keywords = request.keywords
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(keywords)
    extracted_keywords = keyword_processor.extract_keywords(text, span_info=True)

    return {"keywords": extracted_keywords}
