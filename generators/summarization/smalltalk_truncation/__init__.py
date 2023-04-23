from pydantic import BaseModel
from nltk.corpus import stopwords
import re

INPUT_EXAMPLE = {
    "text": '''"Hello, how are you?" he asked.
            "I am doing fine, and you?", she said.
            "I am doing good as well.".
            "Listen, I wanted to talk to you about the something. Actually your car broke down on the bridge and I suspect that the engine is heated up.".
            "Don't worry about that, I'll buy a new car!"''',
    "stopWords": "english",
}


class SmalltalkTruncationModel(BaseModel):
    text: str
    stopWords: str = "english"

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def smalltalk_truncation(request: SmalltalkTruncationModel):
    """Removes all the irrelevant text from a passage or chats"""

    text = request.text
    sw = stopwords.words(request.stopWords)
    regex = re.compile(r"\".*?\"")

    remove_smalltalk = []
    for message in regex.findall(text):
        chat = message.replace('"', '')
        chat = chat.split()
        new_text = []
        stop_words = []
        for token in chat:
            if token not in sw:
                new_text.append(token)
            else:
                stop_words.append(token)
        if (len(new_text) > 0.5 * len(chat) or len(stop_words) > 8) and not len(chat) < 3:
            remove_smalltalk.append(" ".join(chat))

    return {"smalltalkRemoved": remove_smalltalk}
