from pydantic import BaseModel
from extractors.util.spacy import SpacySingleton
import re

INPUT_EXAMPLE = {
    "text": "Leo likes tasty pizza. Mary loves delicious cake. And Moritz loves tasty bread.",
    "spacyTokenizer": "en_core_web_sm",
}

class NounMatchExtractionModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}

def noun_match_extraction(req: NounMatchExtractionModel):
    """Extracts all similar noun chunks from a text"""
    # instantiate empty lists to store already encountered words and for found matches 
    word_repo = []
    matches = []

    text = req.text

    # get noun chunks from spacy 
    nlp = SpacySingleton.get_nlp(req.spacyTokenizer)
    doc = nlp(text.lower())
    nc = [i.text.lower() for i in doc.noun_chunks]
    
    # loop through all noun chunks
    for noun_chunk in nc:
        print(noun_chunk)
        # if noun chunk has more than one word, take first word as a target word
        if len(noun_chunk.split()) >= 2:
            target_word = noun_chunk.split()[0]

            # if target word has been used before, stop process
            if target_word in word_repo:
                pass
            else:
                # pass word to repository to avoid duplicate use
                word_repo.append(target_word)

                # create regex_pattern with target word
                pattern = rf"\W*({target_word})\W*([^\s]+)"
            
                # extract the spans of all found matches
                for item in re.finditer(pattern, text):
                    start, end = item.span()
                    span = doc.char_span(start, end, alignment_mode="expand")
                    matches.append(["match", span.start, span.end])
        else:
            pass

    return {"quote": matches}
