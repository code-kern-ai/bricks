```python

import openai

def gpt_summarizer(text:str, api_key:str, temperature:float = 0) -> str:
    """
    Uses OpenAIs GPT-3.5-turbo model to correct texts. Visit https://platform.openai.com/docs/models/gpt-3-5 for full documentation 
    
    @param text: text you want to extract information from
    @param api_key: OpenAI API key
    @param temperature: OpenAI parameter: Higher values means the model will take more risks. E.g. 0.9 for more creative applications, and 0 for ones with a well-defined answer.
    """
    # Access openai via API key
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""{text}/n/nTl;dr""",
                },
                {
                    "role": "user",
                    "content": f"Text to shorten: {text}",
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
    texts = ["Lloyd Hamilton was one of the most imaginative (and among the funniest) of all the silent-film comedians. Why is he utterly forgotten? Unfortunately, the original negatives for a large percentage of his films were lost when the Fox warehouse burnt in the early 1930s. Hamilton was not handsome or graceful like Chaplin, Keaton and Lloyd; nor was he dapper, like Raymond Griffith. And unlike Harry Langdon and (again) Chaplin, Hamilton did not try for audience sympathy.However, his films were hugely popular at the time of their original release, and they remain hilarious today. Oscar Levant once claimed that he asked Chaplin if there was any other comedian whom he'd ever envied, and Chaplin instantly named Lloyd Hamilton. The character most frequently portrayed by Hamilton on screen, a flat-capped naff, with fastidious hand gestures and a duck-like walk, was later adapted by vaudeville comedian Eddie Garr (Teri Garr's father), and further adapted by Jackie Gleason as his 1950s TV character 'The Poor Soul'."]
    
    api_key = "<API_KEY_GOES_HERE>" # paste your OpenAI API key here
    
    for text in texts:
        print(f"The shorted version of \n\n{text}\n\nis:\n\n{gpt_summarizer(text, api_key)}")
example_integration() 
```