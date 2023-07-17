```python
import openai
import re
import spacy
import os
from typing import List, Tuple

def gpt_information_extraction(text: str, extraction_keyword: str, api_key: str, temperature: float) -> List[Tuple[str, int]]:
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
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(text)

            char_positions = []
            if len(output_dict["keywords"]) > 0:
                for found_keyword in output_dict["keywords"]:
                    regex = re.compile(f"{found_keyword}")
                    match =  regex.search(text)
                    start, end = match.span()
                    span = doc.char_span(start, end, alignment_mode="expand")
                    char_positions.append((extraction_keyword, span.start, span.end)) 
            else:
                return "No matching keywords found."
            return char_positions
        else:
            return f"GPT response was not a valid dictionary. The response was: {response}."
    except: 
        return response["choices"][0]["message"]["content"]

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    # replace this list with a list containing your data
    api_key = "<API_KEY_GOES_HERE>"
    texts = ["I have a dog and two birds", "My favorite animal is the sloth", "Michael Jackson was a singer."]
    
    extraction_keyword = "names of animals"
    for text in texts:
        extraction = gpt_information_extraction(text, extraction_keyword, api_key, temperature=0.0)
        print(f"The text: '{text}' has -> {extraction}")

example_integration()
```