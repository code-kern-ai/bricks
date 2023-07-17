```python
import openai

def gpt_grammar_correction(text:str, api_key:str, temperature:float = 0) -> str:
    """
    Uses OpenAIs GPT-3.5-turbo model to correct texts. Visit https://platform.openai.com/docs/models/gpt-3-5 for full documentation 

    @param text: text you want to extract information from
    @param api_key: OpenAI API key
    @param temperature: OpenAI parameter: Higher values means the model will take more risks. E.g. 0.9 for more creative applications, and 0 for ones with a well-defined answer.

    @return: The corrected text
    """
    # Access openai via API key
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                    Correct this to standard English:\n
                    {text}""",
                },
                {
                    "role": "user",
                    "content": f"Text to correct: {text}",
                },
            ],
            temperature= temperature,
        )
        answer = response["choices"][0]["message"]["content"]
        return {"result": answer}
    except:
        return "That didn't work! Did you provide an OpenAI API key?"
    
   

   
# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():

    texts = ["Named must be your fear before banish it you can."]
    api_key = "<API_KEY_GOES_HERE>" # paste your OpenAI API key here
    
    for text in texts:
        print(f"The corrected version of '{text}' is: {gpt_grammar_correction(text, api_key)}")
example_integration()
```