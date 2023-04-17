import openai
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiKey": "<API_KEY_GOES_HERE>",
    "prompt": "Named must be your fear before banish it you can.",
    "temperature": 0.0,
    "maxTokens": 64,
    "top_p": 1.0,
    "frequencyPenalty": 0.0,
    "presencePenalty": 0.0,
}


class GptGrammarCorrectionModel(BaseModel):
    apiKey: str
    prompt: str
    temperature: float
    maxTokens: int
    top_p: float
    frequencyPenalty: float
    presencePenalty: float

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def gpt_grammar_correction(req: GptGrammarCorrectionModel):
    """GPT-3 model which can be used to classify text inputs."""
    # Access openai via API key
    try:
        openai.api_key = req.apiKey

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""
                Correct this to standard English:\n\n
                {req.prompt}""",
            temperature=req.temperature,
            max_tokens=req.maxTokens,
            top_p=req.top_p,
            frequency_penalty=req.frequencyPenalty,
            presence_penalty=req.presencePenalty,
        )

        return {"Corrected sentence": response["choices"][0]["text"]}

    except:
        return "That didn't work. Did you provide an OpenAI API key?"
