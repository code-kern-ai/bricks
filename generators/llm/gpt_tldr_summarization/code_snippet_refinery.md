```python
import openai

API_KEY: str = "<API_KEY_GOES_HERE>"
ATTRIBUTE: str = "text" # only text attributes
TEMPERATURE: float = 0.0
MAX_TOKENS: int = 60
TOP_P: float = 1.0
FREQUENCY_PENALTY: float = 0.0
PRESENCE_PENALTY: float = 1.0

def gpt_tldr_summarization(record):
    """
    Uses OpenAIs GPT-3 model to classify texts. Visit https://beta.openai.com/docs/api-reference/completions/create for full documentation 

    OpenAI parameters: 
    - temperature: Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer.
    """
    # Access openai via API key
    openai.api_key = API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""{record[ATTRIBUTE].text}/n/nTl;dr""",
                },
                {
                    "role": "user",
                    "content": f"Text to shorten: {text}",
                },
            ],
            temperature= TEMPERATURE,
        )
        answer = response["choices"][0]["message"]["content"]
        return {"result": answer}
    except:
        return "That didn't work! Did you provide an OpenAI API key?"

```
