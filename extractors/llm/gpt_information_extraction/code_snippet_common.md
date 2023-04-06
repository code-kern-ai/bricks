```python
import openai
import re
import spacy

# replace this list with a list containing your data
text = ["My E-Mail address is jane.doe@gmail.com", "Our support mail is support@awesome-co.com"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "api_key": "paste your key here", # paste your OpenAI API key here
    "extraction_keyword": "emails",
    "temperature": 0.0,
    "max_tokens": 64,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
}

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
    openai.api_key = record["api_key"]

    gpt_positions = []
    text_id = 0
    for entry in record["text"]:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""
                Extract all {record["extraction_keyword"]} from this text:\n\n 
                {entry}\n\n
                return {record["extraction_keyword"]} if something is found, else return NAN!""", 
            temperature=record["temperature"],
            max_tokens=record["max_tokens"],
            top_p=record["top_p"],
            frequency_penalty=record["frequency_penalty"],
            presence_penalty=record["presence_penalty"]
        )
        gpt_response = str(response["choices"][0]["text"])
        print(gpt_response)

        nlp = spacy.load("en_core_web_sm")
        doc = nlp(entry)
        
        regex = re.compile(fr"({gpt_response})")
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            gpt_positions.append({f"text_{text_id}" :[record["extraction_keyword"], span.start, span.end]})
        text_id += 1
    return {"extractions": gpt_positions}
```