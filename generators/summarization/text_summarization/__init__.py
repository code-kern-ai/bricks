from pydantic import BaseModel
from generators.util.spacy import SpacySingleton
from string import punctuation
from heapq import nlargest
from spacy.lang.en.stop_words import STOP_WORDS

INPUT_EXAMPLE = {
    "text": """There was a time when he would have embraced the change that was coming. In his youth, he sought 
    adventure and the unknown, but that had been years ago. He wished he could go back and learn to find the 
    excitement that came with change but it was useless. That curiosity had long left him to where he had come to 
    loathe anything that put him out of his comfort zone.""",
    "spacyTokenizer": "en_core_web_sm",
    "length": 0.5,
}


class TextSummarizationModel(BaseModel):
    text: str
    spacyTokenizer: str = "en_core_web_sm"
    length: float

    class Config:
        schema_extra = {
            "example": INPUT_EXAMPLE,
        }


def text_summarization(request: TextSummarizationModel):
    """Generates the summary of a lengthy text"""

    text = request.text
    nlp = SpacySingleton.get_nlp(request.spacyTokenizer)
    doc = nlp(text)
    word_count = {}

    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_count.keys():
                    word_count[word.text] = 1
                else:
                    word_count[word.text] += 1

    maximum_count = max(word_count.values())

    for word in word_count.keys():
        word_count[word] = word_count[word] / maximum_count

    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}

    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_count.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_count[word.text.lower()]
                else:
                    sentence_scores[sent] += word_count[word.text.lower()]

    size = int(len(sentence_tokens) * request.length)
    extracted_sentences = nlargest(size, sentence_scores, key=sentence_scores.get)
    summarise = [word.text for word in extracted_sentences]
    summary = " ".join(summarise)

    return {"summary": summary}
