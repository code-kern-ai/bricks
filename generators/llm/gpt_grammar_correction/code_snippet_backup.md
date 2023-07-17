```python
import openai

# replace this list with a list containing your data
text = ["Named must be your fear before banish it you can."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "api_key": "paste your api key here",
    "temperature": 0
}

def gpt_grammar_correction(record):
    """
    Uses OpenAIs GPT-3.5-turbo model to correct texts. Visit https://platform.openai.com/docs/models/gpt-3-5 for full documentation 

    OpenAI parameters: 
    - temperature: Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer.

    """
    # Access openai via API key
    openai.api_key = record["api_key"]
    
    corrected_texts = []
    try:
        for entry in record["text"]:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": f"""
                        Correct this to standard English:\n
                        {entry}""",
                    },
                    {
                        "role": "user",
                        "content": f"Text to correct: {entry}",
                    },
                ],
                temperature=record["temperature"],
            )
            answer = response["choices"][0]["message"]["content"]
            corrected_texts.append(answer)
        return {"result": corrected_texts}
    except:
        return "That didn't work! Did you provide an OpenAI API key?"
    
```