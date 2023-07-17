```python
import openai

# replace this list with a list containing your data
text = ["Lloyd Hamilton was one of the most imaginative (and among the funniest) of all the silent-film comedians. Why is he utterly forgotten? Unfortunately, the original negatives for a large percentage of his films were lost when the Fox warehouse burnt in the early 1930s. Hamilton was not handsome or graceful like Chaplin, Keaton and Lloyd; nor was he dapper, like Raymond Griffith. And unlike Harry Langdon and (again) Chaplin, Hamilton did not try for audience sympathy.However, his films were hugely popular at the time of their original release, and they remain hilarious today. Oscar Levant once claimed that he asked Chaplin if there was any other comedian whom he'd ever envied, and Chaplin instantly named Lloyd Hamilton. The character most frequently portrayed by Hamilton on screen, a flat-capped naff, with fastidious hand gestures and a duck-like walk, was later adapted by vaudeville comedian Eddie Garr (Teri Garr's father), and further adapted by Jackie Gleason as his 1950s TV character 'The Poor Soul'."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "api_key": "paste your api key here",
    "temperature": 0.0,
}

def gpt_summarizer(record):
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
                    "content": f"""{entry}/n/nTl;dr""",
                },
                {
                    "role": "user",
                    "content": f"Text to shorten: {entry}",
                },
            ],
            temperature= record["temperature"],
        )
        answer = response["choices"][0]["message"]["content"]
        corrected_texts.append(answer)
        return {"result": corrected_texts}
    except:
        return "That didn't work! Did you provide an OpenAI API key?"

```