```python
import openai
import re

# replace this list with a list containing your data
texts = ["This is a positve text.", "This is a negative text."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": texts,
    "api_key": "paste your api key here",
    "classify_by": "emotional sentiment",
    "labels": ["positive", "neutral", "negative"],
    "temperature": 0.0,
    "max_tokens": 64,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
}

def gpt_classifier(record):
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
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a classification assistant and need to classify texts based on their {classify_by}. You may only return one of these labels: {', '.join(labels)}. \
                                Return nothing execpt one of the mentioned labels. The output should only contain a single word.",
                },
                {
                    "role": "user",
                    "content": f"Text to classify: {text}",
                },
            ],
            temperature=0,
        )
        answer = response["choices"][0]["message"]["content"]
        return answer
    except:
        return "That didn't work! Did you provide an OpenAI API key?"
```