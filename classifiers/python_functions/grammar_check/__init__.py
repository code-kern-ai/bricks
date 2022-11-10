from pydantic import BaseModel
import language_tool_python

INPUT_EXAMPLE = {
    "text": "This is a test test string, to test the gramatical errors.",
    "language": "en-US",
}


class GrammarCheckModel(BaseModel):
    text: str
    language: str = "en-US"

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def grammar_check(request: GrammarCheckModel):
    """Check for grammatical mistakes in a text."""

    text = request.text
    lang = language_tool_python.LanguageTool(request.language)
    my_match = lang.check(text)

    startPos = []
    endPos = []
    mistakes = []
    corrections = []

    for rules in my_match:
        if len(rules.replacements) > 0:
            startPos.append(rules.offset)
            endPos.append(rules.errorLength + rules.offset)
            mistakes.append(text[rules.offset: rules.errorLength + rules.offset])
            corrections.append(rules.replacements[0])

    corrected_text = list(text)

    for n, _ in enumerate(startPos):
        for i, _ in enumerate(text):
            corrected_text[startPos[n]] = corrections[n]
            if startPos[n] < i < endPos[n]:
                corrected_text[i] = ""

    corrected_text = "".join(corrected_text)

    return {
        "mistakes": mistakes,
        "suggestedCorrections": corrections,
        "correctedText": corrected_text
    }
