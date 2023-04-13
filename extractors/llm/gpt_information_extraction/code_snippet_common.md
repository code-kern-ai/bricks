```python
from typing import Tuple, List
import openai
import re
import spacy

def gpt_information_extraction(text:str, extraction_keyword:str, api_key:str, temperature:float = 0.0, max_tokens:int = 64, top_p:float = 1.0, frequency_penalty:float = 0.0, presence_penalty:float = 0.0) -> List[Tuple[str,int]]:
    """
    Uses OpenAIs GPT-3 model to extract information from texts. Visit https://beta.openai.com/docs/api-reference/completions/create for full documentation 

    @param text: text you want to extract information from
    @param extraction_keyword: keyword to extract
    @param api_key: OpenAI API key
    @param temperature: OpenAI parameter: Higher values means the model will take more risks. E.g. 0.9 for more creative applications, and 0 for ones with a well-defined answer.
    @param max_tokens: OpenAI parameter: The maximum number of tokens to generate in the completion.
    @param top_p: OpenAI parameter: Amount of tokens the model considers.
    @param frequency_penalty: OpenAI parameter: Value between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency, decreasing the model's likelihood to repeat the same line verbatim.
    @param presence_penalty: OpenAI parameter: Value between -2.0 and 2.0. Positive values penalize new tokens based on their existing presence (in other words, if you had the choice between two completions, and one of them used a word that you already used in the prompt, the model will be less likely to choose that completion). Decreasing the value of this parameter will make the model more likely to repeat words it has already used.
    @return: A List of all found emails and their spacy token start and end index
    """
    openai.api_key = api_key

    gpt_positions = []
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
            Extract all {extraction_keyword} from this text:\n\n 
            {text}\n\n
            return {extraction_keyword} if something is found, else return NAN!""", 
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    gpt_response = str(response["choices"][0]["text"])

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    gpt_positions = []
    regex = re.compile(fr"({gpt_response})")
    for match in regex.finditer(text):
        start, end = match.span()
        span = doc.char_span(start, end, alignment_mode="expand")
        gpt_positions.append((extraction_keyword, span.start, span.end))
    return gpt_positions


# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():

    texts = ["My E-Mail address is jane.doe@gmail.com", "Our support mail is support@awesome-co.com", "This is a negative text."]
    api_key = "<API_KEY_TO_USE>" # paste your OpenAI API key here
    extraction_keyword = "emails"
    
    for text in texts:
        found = gpt_information_extraction(text, extraction_keyword, api_key)
        if found:
            print(f"text: \"{text}\" has {extraction_keyword} \"{found}\"")
        else:
            print(f"text: \"{text}\" doesn't have {extraction_keyword}")

example_integration()
```