```python
import openai

YOUR_API_KEY: str = "<API_KEY_GOES_HERE>"
YOUR_ATTRIBUTE: str = "text"
YOUR_TEMPERATURE: int = 0
YOUR_MAX_TOKENS: int = 64
YOUR_TOP_P: float = 1.0
YOUR_FREQUENCY_PENALTY: float = 0.0
YOUR_PRESENCE_PENALTY: float = 0.0

def gpt3_classifier(record):
    # Access openai via API key
    openai.api_key = YOUR_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
            Correct this to standard English:\n
            {record[YOUR_ATTRIBUTE].text}""",
        temperature=YOUR_TEMPERATURE,
        max_tokens=YOUR_MAX_TOKENS,
        top_p=YOUR_TOP_P,
        frequency_penalty=YOUR_FREQUENCY_PENALTY,
        presence_penalty=YOUR_PRESENCE_PENALTY
    )

    return response
```
