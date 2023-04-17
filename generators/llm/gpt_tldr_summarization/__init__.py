import openai
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiKey": "<API_KEY_GOES_HERE>",
    "prompt": "Lloyd Hamilton was one of the most imaginative (and among the funniest) of all the silent-film comedians. Why is he utterly forgotten? Unfortunately, the original negatives for a large percentage of his films were lost when the Fox warehouse burnt in the early 1930s. Hamilton was not handsome or graceful like Chaplin, Keaton and Lloyd; nor was he dapper, like Raymond Griffith. And unlike Harry Langdon and (again) Chaplin, Hamilton did not try for audience sympathy.However, his films were hugely popular at the time of their original release, and they remain hilarious today. Oscar Levant once claimed that he asked Chaplin if there was any other comedian whom he'd ever envied, and Chaplin instantly named Lloyd Hamilton. The character most frequently portrayed by Hamilton on screen, a flat-capped naff, with fastidious hand gestures and a duck-like walk, was later adapted by vaudeville comedian Eddie Garr (Teri Garr's father), and further adapted by Jackie Gleason as his 1950s TV character 'The Poor Soul'.",
    "temperature": 0.0,
    "maxTokens": 60,
    "top_p": 1.0,
    "frequencyPenalty": 0.0,
    "presencePenalty": 1,
}


class GptTldrSummarizationModel(BaseModel):
    apiKey: str
    prompt: str
    temperature: float
    maxTokens: int
    top_p: float
    frequencyPenalty: float
    presencePenalty: float

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def gpt_tldr_summarization(req: GptTldrSummarizationModel):
    """GPT-3 model which can be used to summarise text inputs."""
    # Access openai via API key
    try:
        openai.api_key = req.apiKey

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""
                {req.prompt}\n\nTl;dr""",
            temperature=req.temperature,
            max_tokens=req.maxTokens,
            top_p=req.top_p,
            frequency_penalty=req.frequencyPenalty,
            presence_penalty=req.presencePenalty,
        )

        return {"Summarised text": response["choices"][0]["text"]}

    except:
        return "That didn't work. Did you provide an OpenAI API key?"
