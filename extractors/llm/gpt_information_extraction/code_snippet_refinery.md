```python
import openai
import re
import json

API_KEY: str = "<API_KEY_GOES_HERE>"
ATTRIBUTE: str = "text" # only text attributes
EXTRACTION_KEYWORD: str = "names"
TEMPERATURE: int = 0.0
MAX_TOKENS: int = 64
TOP_P: float = 1.0
FREQUENCY_PENALTY: float = 0.0
PRESENCE_PENALTY: float = 0.0
LABEL: str = "name"

def gpt_information_extraction(record):
    """
    Uses OpenAIs GPT-3 model to classify texts. Visit https://beta.openai.com/docs/api-reference/completions/create for full documentation 

    OpenAI parameters: 
    - temperature: Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer.

    - max_tokens: The maximum number of tokens to generate in the completion.

    - top_p: Amount of tokens the model considers.

    - frequency_penalty: Value between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency, decreasing the model's likelihood to repeat the same line verbatim.

    - presence_penalty: Value between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
    """
    # Access openai via API key
    text = record[ATTRIBUTE].text
    openai.api_key = API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
            Extract all {EXTRACTION_KEYWORD} from this text:\n\n
            {text}\n\n
            return a list of json objects with the keys {EXTRACTION_KEYWORD} and charPosition the {EXTRACTION_KEYWORD} was found. 
            If nothing is found return NAN!""", 
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY
    )
    gpt_response = response["choices"][0]["text"].strip().replace("'","\"")
    if gpt_response == "NAN!":
        return []
    parsed = json.loads(gpt_response)
    if len(parsed) == 0:
        return []
    # find used json key (since e.g. emails will become email)
    json_key = EXTRACTION_KEYWORD
    if EXTRACTION_KEYWORD not in parsed[0]:        
        for key in parsed[0]:
            if key != "charPosition":
                json_key = key
                break
    #gpt can't reliably find the correct position since the whole prompt is used so we need to find the difference and apply it
    char_pos_diff = parsed[0]["charPosition"] - text.index(parsed[0][json_key])    
    for match in parsed:
        start = match["charPosition"] - char_pos_diff
        end = start + len(match[json_key]) - 1
        span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        if span:
            yield LABEL, span.start, span.end


```