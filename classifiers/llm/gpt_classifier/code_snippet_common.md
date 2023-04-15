```python
from typing import List, Tuple
import openai
import re


def gpt_classifier(text:str, classify_by:str, labels:List[str], api_key:str, temperature:float = 0.0, max_tokens:int = 64, top_p:float = 1.0, frequency_penalty:float = 0.0, presence_penalty:float = 0.0) -> str:
    """
    Uses OpenAIs GPT-3 model to classify texts. Visit https://beta.openai.com/docs/api-reference/completions/create for full documentation 

    @param text: text you want to extract information from
    @param classify_by: keyword to extract
    @param labels: labels to choose from
    @param api_key: OpenAI API key
    @param temperature: OpenAI parameter: Higher values means the model will take more risks. E.g. 0.9 for more creative applications, and 0 for ones with a well-defined answer.
    @param max_tokens: OpenAI parameter: The maximum number of tokens to generate in the completion.
    @param top_p: OpenAI parameter: Amount of tokens the model considers.
    @param frequency_penalty: OpenAI parameter: Value between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency, decreasing the model's likelihood to repeat the same line verbatim.
    @param presence_penalty: OpenAI parameter: Value between -2.0 and 2.0. Positive values penalize new tokens based on their existing presence (in other words, if you had the choice between two completions, and one of them used a word that you already used in the prompt, the model will be less likely to choose that completion). Decreasing the value of this parameter will make the model more likely to repeat words it has already used.
    @return: The found label
    """
    # Access openai via API key
    openai.api_key = api_key
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""
                The following sentence will be classfied by {classify_by}:\n\n
                {text}\n
                use the following labels: {", ".join(labels)}:""",
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
    return response["choices"][0]["text"].strip().lower()

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():

    texts = ["This is a positve text.", "This is a negative text."]
    api_key = "<API_KEY_TO_USE>" # paste your OpenAI API key here
    classify_by = "emotional sentiment"
    labels = ["positive", "neutral", "negative"]
    extraction_keyword = "emails"
    
    for text in texts:
        print(f"the {classify_by} of \"{text}\" is {gpt_classifier(text, classify_by, labels, api_key)}")

example_integration()
```