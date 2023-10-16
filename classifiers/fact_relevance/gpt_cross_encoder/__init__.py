import openai
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "question": "I would like to learn more about the insurance policy.",
    "fact": "Section A1.2 of our Global Explorer travel insurance: The insurance covers up to 100.000 EUR of damages while traveling abroad.",
    "api_key": "<API_KEY_GOES_HERE>",
    "temperature": 0.0,
}


class GptCrossEncoderModel(BaseModel):
    question: str
    fact: str
    api_key: str
    temperature: float

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def gpt_cross_encoder(req: GptCrossEncoderModel):
    """Uses GPT as a cross-encoder to get the relevance of a fact to a question"""
    openai.api_key = req.api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"""
                    Take a breath. You are assessing the relevance of question-fact pairs.
                    If a fact is directly related to the topic of the question (e.g. directly or even by implying consequences), it is "Relevant".
                    If there is no connection, it is "Irrelevant". In case of doubt, the fact is "Irrelevant".

                        Fact: {req.fact}
                        Question: {req.question}

                    Determine the relevance. Give a score from 0 to 100 for this (100 would be a straight answer to the question). 
                    Answer ONLY with the score itself (i.e. a number between 0 and 100).
                    If you answer with more than one number between 0 and 100, I will not process your output!""",
            },
        ],
        temperature=req.temperature,
    )
    answer = response["choices"][0]["message"]["content"]

    if int(answer) > 50:
        return "Yes"
    return "No"