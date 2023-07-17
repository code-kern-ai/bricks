import openai
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiKey": "<API_KEY_GOES_HERE>",
    "text": "Named must be your fear before banish it you can.",
    "temperature": 0.0,
}


class GptGrammarCorrectionModel(BaseModel):
    apiKey: str
    text: str
    temperature: float

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def gpt_grammar_correction(req: GptGrammarCorrectionModel):
    """GPT-3.5 model which can be used to correct grammar."""
    openai.api_key = req.apiKey
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                    Correct this to standard English:\n
                    {req.text}""",
                },
                {
                    "role": "user",
                    "content": f"Text to correct: {req.text}",
                },
            ],
            temperature=req.temperature,
        )
        answer = response["choices"][0]["message"]["content"]
        return {"result": answer}
    except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e}"
