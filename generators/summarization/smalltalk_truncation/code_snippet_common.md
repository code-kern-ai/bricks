```python 
import re
from nltk.corpus import stopwords

sw = set(stopwords.words("english"))
regex = re.compile(r"\".*?\"")
def smalltalk_truncation(text:str):
    """
    @param text: text to truncate
    @return: truncated text
    """
    removed_smalltalk = []
    for message in regex.findall(text):
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
            removed_smalltalk.append(" ".join(chat))

    return removed_smalltalk

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    texts = ['''"Hello, how are you?" he asked.
"I am doing fine, and you?", she said.
"I am doing good as well.".
"Listen, I wanted to talk to you about the something. Actually your car broke down on the bridge and I suspect that the engine is heated up.".
"Don't worry about that, I'll buy a new car!"''']

    for text in texts:
        print(f"the truncated version of \n\n{text}\n\nis:\n{smalltalk_truncation(text)}")
example_integration() 
```