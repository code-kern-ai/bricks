```python
import openai

def gpt_summarizer(text:str, api_key:str, temperature:float = 0.0, max_tokens:int = 64, top_p:float = 1.0, frequency_penalty:float = 0.0, presence_penalty:float = 0.0) -> str:
    """
    Uses OpenAIs GPT-3 model to summarize texts. Visit https://beta.openai.com/docs/api-reference/completions/create for full documentation 

    @param text: text you want to extract information from
    @param api_key: OpenAI API key
    @param temperature: OpenAI parameter: Higher values means the model will take more risks. E.g. 0.9 for more creative applications, and 0 for ones with a well-defined answer.
    @param max_tokens: OpenAI parameter: The maximum number of tokens to generate in the completion.
    @param top_p: OpenAI parameter: Amount of tokens the model considers.
    @param frequency_penalty: OpenAI parameter: Value between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency, decreasing the model's likelihood to repeat the same line verbatim.
    @param presence_penalty: OpenAI parameter: Value between -2.0 and 2.0. Positive values penalize new tokens based on their existing presence (in other words, if you had the choice between two completions, and one of them used a word that you already used in the prompt, the model will be less likely to choose that completion). Decreasing the value of this parameter will make the model more likely to repeat words it has already used.
    @return: The corrected text
    """
    # Access openai via API key
    openai.api_key = api_key
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""{text}/n/nTl;dr""",
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
    return response["choices"][0]["text"].strip()
      
# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["Lloyd Hamilton was one of the most imaginative (and among the funniest) of all the silent-film comedians. Why is he utterly forgotten? Unfortunately, the original negatives for a large percentage of his films were lost when the Fox warehouse burnt in the early 1930s. Hamilton was not handsome or graceful like Chaplin, Keaton and Lloyd; nor was he dapper, like Raymond Griffith. And unlike Harry Langdon and (again) Chaplin, Hamilton did not try for audience sympathy.However, his films were hugely popular at the time of their original release, and they remain hilarious today. Oscar Levant once claimed that he asked Chaplin if there was any other comedian whom he'd ever envied, and Chaplin instantly named Lloyd Hamilton. The character most frequently portrayed by Hamilton on screen, a flat-capped naff, with fastidious hand gestures and a duck-like walk, was later adapted by vaudeville comedian Eddie Garr (Teri Garr's father), and further adapted by Jackie Gleason as his 1950s TV character 'The Poor Soul'."]
    
    api_key = "<API_KEY_TO_USE>" # paste your OpenAI API key here
    
    for text in texts:
        print(f"The shorted version of \n\n{text}\n\nis:\n\n{gpt_summarizer(text, api_key)}")
example_integration() 
```