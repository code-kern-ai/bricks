```python
import openai

# replace this list with a list containing your data
text = ["Lloyd Hamilton was one of the most imaginative (and among the funniest) of all the silent-film comedians. Why is he utterly forgotten? Unfortunately, the original negatives for a large percentage of his films were lost when the Fox warehouse burnt in the early 1930s. Hamilton was not handsome or graceful like Chaplin, Keaton and Lloyd; nor was he dapper, like Raymond Griffith. And unlike Harry Langdon and (again) Chaplin, Hamilton did not try for audience sympathy.However, his films were hugely popular at the time of their original release, and they remain hilarious today. Oscar Levant once claimed that he asked Chaplin if there was any other comedian whom he'd ever envied, and Chaplin instantly named Lloyd Hamilton. The character most frequently portrayed by Hamilton on screen, a flat-capped naff, with fastidious hand gestures and a duck-like walk, was later adapted by vaudeville comedian Eddie Garr (Teri Garr's father), and further adapted by Jackie Gleason as his 1950s TV character 'The Poor Soul'."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "api_key": "paste your api key here",
    "temperature": 0.0,
    "max_tokens": 64,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0
}

def gpt_summarizer(record):
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

    corrected_texts = []
    for entry in record["text"]:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""{entry}/n/nTl;dr""",
            temperature=record["temperature"],
            max_tokens=record["max_tokens"],
            top_p=record["top_p"],
            frequency_penalty=record["frequency_penalty"],
            presence_penalty=record["presence_penalty"]
        )
        corrected_texts.append(response["choices"][0]["text"])
    return {"tldrResults": corrected_texts}
```