``` python
import openai
import re
import spacy
from typing import List, Tuple
import ast
import re

API_KEY: str = "<API_KEY_GOES_HERE>"
ATTRIBUTE: str = "text" # only text attributes
EXTRACTION_KEYWORDS: List = ["insurance companies", "insured company", "website of insured company", "address of insured company", "type of coverage", "date of submission", "amount of revenue", "description of insured company"]
TEMPERATURE: float = 0.0

def insurance_email_extraction(record):
    text = record[ATTRIBUTE].text
    openai.api_key = API_KEY
    for extraction in EXTRACTION_KEYWORDS:
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {
                    "role": "system",
                    "content":   f"""
                        Please extract all {extraction} from following text:
                        {text}-
                        Only return things that are linked to {extraction}.
                        Return only a valid JSON with this structure. 
                        json
                        {{
                            "keywords": ["list with keywords goes here"]
                        }}
                        
                        Return nothing except this JSON. Make sure to only return {extraction} and nothing else. 
                        If you can't find any {extraction} in the text, just return nothing."""
                    ,
                },
            ],
            temperature=TEMPERATURE,
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
                    #char_positions.append((extraction_keyword, span.start, span.end)) 
                    char_positions.append((match[0], span.start, span.end)) 
            else:
                return "No matching keywords found."
            return char_positions
        else:
            return f"GPT response was not a valid dictionary. The response was: {response}."
    except: 
        return response["choices"][0]["message"]["content"]

```