import openai
from litellm import completion
from pydantic import BaseModel
from typing import List

INPUT_EXAMPLE = {
    "apiKey": "<API_KEY_GOES_HERE>",
    "text": "I had a really great day today!",
    "classifyBy": "sentiment",
    "temperature": 0.0,
    "labels": ["positive", "neutral", "negative"]
}


class GptClassifierModel(BaseModel):
    apiKey: str
    text: str
    classifyBy: str
    temperature: float
    labels: List

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def gpt_classifier(req: GptClassifierModel):
    """GPT model which can be used to correct the grammar of text inputs."""

    openai.api_key = req.apiKey
    try:
        response = completion(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a classification assistant and need to classify texts based on their {req.classifyBy}. You may only return one of these labels: {', '.join(req.labels)}. \
                                Return nothing execpt one of the mentioned labels. The output should only contain a single word.",
                },
                {
                    "role": "user",
                    "content": f"Text to classify: {req.text}",
                },
            ],
            temperature=req.temperature,
        )
        answer = response["choices"][0]["message"]["content"]
        return {"result": answer}
    except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response}"
