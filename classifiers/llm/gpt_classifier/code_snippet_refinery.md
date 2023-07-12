```python
import openai
from typing import List

API_KEY: str = "<OPENAI_KEY_HERE>"
ATTRIBUTE: str = "text" # only text attributes
CLASSIFY_BY: str = "sentiment" # change this to whatever you want to get classified by (sentiment, toxicity, etc.)
TEMPERATURE: float = 0.0 
LABELS: List = ["positive", "neutral", "negative"] # change this to the labels you want to classify by

def gpt_classifier(record):
    """
    Uses OpenAIs GPT-3.5-turbo model to classify texts. Visit https://platform.openai.com/docs/models/gpt-3-5 for full documentation 

    OpenAI parameters: 
    - temperature: Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer.
    """
    openai.api_key = API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a classification assistant and need to classify texts based on their {CLASSIFY_BY}. You may only return one of these labels: {', '.join(LABELS)}. \
                                Return nothing execpt one of the mentioned labels. The output should only contain a single word.",
                },
                {
                    "role": "user",
                    "content": f"Text to classify: {record[ATTRIBUTE].text}",
                },
            ],
            temperature=TEMPERATURE,
        )
        answer = response["choices"][0]["message"]["content"]
        return answer
    except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response}"
```