```python
import openai
import re

YOUR_API_KEY: str = "<API_KEY_GOES_HERE>"
YOUR_ATTRIBUTE: str = "text" # only text attributes
YOUR_EXTRACTION_KEYWORD: str = "names"
YOUR_TEMPERATURE: int = 0.0
YOUR_MAX_TOKENS: int = 64
YOUR_TOP_P: float = 1.0
YOUR_FREQUENCY_PENALTY: float = 0.0
YOUR_PRESENCE_PENALTY: float = 0.0
YOUR_LABEL: str = "keyinfo"

def gpt3_information_extraction(record):
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
    if not record[YOUR_ATTRIBUTE] or not record[YOUR_ATTRIBUTE].text:
        return "No text string read!"
    text = record[YOUR_ATTRIBUTE].text
    openai.api_key = YOUR_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
            Extract all {YOUR_EXTRACTION_KEYWORD} from this text:\n\n 
            {text}\n\n
            return {YOUR_EXTRACTION_KEYWORD} if something is found, else return NAN!""", 
        temperature=YOUR_TEMPERATURE,
        max_tokens=YOUR_MAX_TOKENS,
        top_p=YOUR_TOP_P,
        frequency_penalty=YOUR_FREQUENCY_PENALTY,
        presence_penalty=YOUR_PRESENCE_PENALTY
    )
    gpt_response = str(response["choices"][0]["text"])
    
    re_comp = re.compile(fr"({gpt_response})")
    match = re_comp.search( text.lower())
    if match:
        start, end = match.start(), match.end()
        span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")
        yield YOUR_LABEL, span.start, span.end
```