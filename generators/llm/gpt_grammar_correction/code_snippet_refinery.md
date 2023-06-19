```python
import openai

API_KEY: str = "<API_KEY_GOES_HERE>"
ATTRIBUTE: str = "text" # only text attributes
TEMPERATURE: float = 0.0


def gpt_grammar_correction(record):
    """
    Uses OpenAIs GPT-3.5-turbo model to correct texts. Visit https://platform.openai.com/docs/models/gpt-3-5 for full documentation 

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
                    "content": f"""
                    Correct this to standard English:\n
                    {record[ATTRIBUTE].text}""",
                },
                {
                    "role": "user",
                    "content": f"Text to correct: {record[ATTRIBUTE].text}",
                },
            ],
            temperature = TEMPERATURE,
        )
        answer = response["choices"][0]["message"]["content"]
        return answer

```
