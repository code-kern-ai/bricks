```python 
import re
from nltk.corpus import stopwords

# replace this list with a list containing your data
text = ['''"Hello, how are you?" he asked.
            "I am doing fine, and you?", she said.
            "I am doing good as well.".
            "Listen, I wanted to talk to you about the something. Actually your car broke down on the bridge and I suspect that the engine is heated up.".
            "Don't worry about that, I'll buy a new car!"''']

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def smalltalk_truncation(record):
    sw = stopwords.words("english")
    regex = re.compile(r"\".*?\"")

    truncated_text = []
    for entry in record["text"]:
        for message in regex.findall(entry):
            chat = message.replace('"','')
            chat = chat.split()
            new_text = []
            stop_words = []
            for token in chat:
                if token not in sw:
                    new_text.append(token)
                else:
                    stop_words.append(token)
            if (len(new_text) > 0.5*len(chat) or len(stop_words) > 8) and not len(chat) < 3:
                truncated_text.append(" ".join(chat))

    return {"truncatedText": truncated_text}
```