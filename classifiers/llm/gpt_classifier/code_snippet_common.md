```python
from typing import List, Tuple
import openai
import re


def gpt_classifier(text:str, classify_by:str, labels:List[str], api_key:str, temperature:float = 0.0) -> str:
    """
    Uses OpenAIs GPT-3.5-turbo model to classify texts. Visit https://platform.openai.com/docs/models/gpt-3-5 for full documentation 

    @param text: text you want to extract information from
    @param classify_by: keyword to extract
    @param labels: labels to choose from
    @param api_key: OpenAI API key
    @param temperature: OpenAI parameter: Higher values means the model will take more risks. E.g. 0.9 for more creative applications, and 0 for ones with a well-defined answer.
    @return: The found label
    """
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a classification assistant and need to classify texts based on their {classify_by}. You may only return one of these labels: {', '.join(labels)}. \
                                Return nothing execpt one of the mentioned labels. The output should only contain a single word.",
                },
                {
                    "role": "user",
                    "content": f"Text to classify: {text}",
                },
            ],
            temperature=0,
        )
        answer = response["choices"][0]["message"]["content"]
        return {"result": answer}
    except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response}"
        


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():

    texts = ["Wow this is a really delicious ice cream!", "Worst. Movie. Ever!"]
    api_key = "<OPENAI_API_KEY>" # paste your OpenAI API key here
    classify_by = "emotional sentiment"
    labels = ["positive", "neutral", "negative"]
    
    for text in texts:
        print(f"the {classify_by} of \"{text}\" is {gpt_classifier(text, classify_by, labels, api_key)}")

example_integration()
```