import re

from pydantic import BaseModel
from typing import Optional

from nltk.corpus import wordnet
from extractors.util.spacy import SpacySingleton

INPUT_EXAMPLE = {
    "targetWord": "Soccer",
    "text": "My sister is good at playing football.",
    "spacyTokenizer": "en_core_web_sm",
}

class SynonymExtractionModel(BaseModel):
    targetWord: str
    text: str
    spacyTokenizer: Optional[str] = "en_core_web_sm"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def synonym_extraction(SynonymExtractionModel):
    '''Finds and extracts synonyms using Wordnet.'''
    # Word that we would like to find synonyms to
    target_word = SynonymExtractionModel.targetWord

    # Find synonyms using wordnet
    synonyms = []
    for syn in wordnet.synsets(target_word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    # The text we would like to go through
    text = SynonymExtractionModel.text

    # Word are sometimes connected by a _, which we want to remove      
    split_synonyms = [item.split(sep="_") for item in synonyms]

    # Break up potential list of lists into a single list
    combined_synonyms = [item for sublist in split_synonyms for item in sublist]

    nlp = SpacySingleton.get_nlp(SynonymExtractionModel.spacyTokenizer)
    doc = nlp(text)

    # Get the span of found matches
    synonym_matches = []
    for word in combined_synonyms:
        try:
            pattern = rf"({word})"
            match = re.search(pattern, text)

            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")

            synonym_matches.append(["synonym", span.start, span.end])
        except:
            pass

    return {"synonyms": synonym_matches}
