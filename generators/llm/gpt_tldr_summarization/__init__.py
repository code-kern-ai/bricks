import openai
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiKey": "<API_KEY_GOES_HERE>",
    "prompt": "Lloyd Hamilton was one of the most imaginative (and among the funniest) of all the silent-film comedians. Why is he utterly forgotten? Unfortunately, the original negatives for a large percentage of his films were lost when the Fox warehouse burnt in the early 1930s. Hamilton was not handsome or graceful like Chaplin, Keaton and Lloyd; nor was he dapper, like Raymond Griffith. And unlike Harry Langdon and (again) Chaplin, Hamilton did not try for audience sympathy.However, his films were hugely popular at the time of their original release, and they remain hilarious today. Oscar Levant once claimed that he asked Chaplin if there was any other comedian whom he'd ever envied, and Chaplin instantly named Lloyd Hamilton. The character most frequently portrayed by Hamilton on screen, a flat-capped naff, with fastidious hand gestures and a duck-like walk, was later adapted by vaudeville comedian Eddie Garr (Teri Garr's father), and further adapted by Jackie Gleason as his 1950s TV character 'The Poor Soul'.",
    "temperature": 0.0,
}


class GptTldrSummarizationModel(BaseModel):
    apiKey: str
    prompt: str
    temperature: float

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def gpt_tldr_summarization(req: GptTldrSummarizationModel):
    """GPT-3.5 model which can be used to summarize text inputs."""
    openai.api_key = req.apiKey
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""{req.text}/n/nTl;dr""",
                },
                {
                    "role": "user",
                    "content": f"Text to shorten: {req.text}",
                },
            ],
            temperature= req.temperature,
        )
        answer = response["choices"][0]["message"]["content"]
        return {"Summarised text": answer}

    except:
        return "That didn't work. Did you provide an OpenAI API key?"
