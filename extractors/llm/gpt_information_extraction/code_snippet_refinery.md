```python
import openai
import re
import json

API_KEY: str = "<API_KEY_GOES_HERE>"
ATTRIBUTE: str = "text" # only text attributes
EXTRACTION_KEYWORD: str = "names"
TEMPERATURE: float = 0.0

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
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "system",
                "content":   f"""
                    Please extract all {extraction_keyword} from following text:
                    {text}-
                    Only return things that are linked to {extraction_keyword}.
                    Return only a valid JSON with this structure. 
                    ```json
                    {{
                        "keywords": ["list with keywords goes here"]
                    }}
                    ```
                    Return nothing except this JSON. Make sure to only return {extraction_keyword} and nothing else. 
                    If you can't find any {extraction_keyword} in the text, just return nothing."""
                ,
            },
        ],
        temperature=temperature,
    )
    try: 
        out = response["choices"][0]["message"]["content"]
        output_dict = ast.literal_eval(out)

        # check if the output is really a dictionary
        if isinstance(output_dict, dict):
            if len(output_dict["keywords"]) > 0:
                for found_keyword in output_dict["keywords"]:
                    regex = re.compile(f"{found_keyword}")
                    match =  regex.search(text)
                    start, end = match.span()
                    span = record[ATTRIBUTE].char_span(start, end, alignment_mode="expand")
                    yield extraction_keyword, span.start, span.end
            else:
                return "No matching keywords found."
        else:
            return f"GPT response was not a valid dictionary. The response was: {response}."
    except: 
        return response["choices"][0]["message"]["content"]
```