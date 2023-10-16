```python
import openai
import os 

ATTRIBUTE: str = "text" 
FACT: str = "fact"
API_KEY: str = "<API_KEY_GOES_HERE>"
API_BASE: str = "https://api.openai.com/v1"
API_TYPE: str = "open_ai" # or 'azure'
API_VERSION: str = None
ENGINE: str = None
TEMPERATURE: float = 0.0

openai.api_key = API_KEY
openai.api_base = API_BASE
openai.api_type = API_TYPE
openai.api_version = API_VERSION

def gpt_cross_encoder(record):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        engine=ENGINE,
        messages=[
            {
                "role": "system",
                "content": f"""
                    Take a breath. You are assessing the relevance of question-fact pairs.
                    If a fact is directly related to the topic of the question (e.g. directly or even by implying consequences), it is "Relevant".
                    If there is no connection, it is "Irrelevant". In case of doubt, the fact is "Irrelevant".

                        Fact: {record[FACT].text}
                        Question: {record[ATTRIBUTE].text}

                    Determine the relevance. Give a score from 0 to 100 for this (100 would be a straight answer to the question). 
                    Answer ONLY with the score itself (i.e. a number between 0 and 100).
                    If you answer with more than one number between 0 and 100, I will not process your output!""",
            },
            # {
            #     "role": "user",
            #     "content": f"Text to classify: {text}",
            # },
        ],
        temperature=TEMPERATURE,
    )
    answer = response["choices"][0]["message"]["content"]

    if int(answer) > 50:
        return "Yes"
    return "No"
```