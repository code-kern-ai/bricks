import openai
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiKey": "<API_KEY_GOES_HERE>",
    "prompt": "Name: Tuscolo\nPizza amazing, too many people, quick service, moderately expensive.",
    "temperature": 0.5,
    "maxTokens": 64,
    "top_p": 1.0,
    "frequencyPenalty": 0.0,
    "presencePenalty": 1
}


class Gpt3RestaurantReviewModel(BaseModel):
    apiKey: str
    prompt: str
    temperature: float
    maxTokens: int
    top_p: float
    frequencyPenalty: float
    presencePenalty: float

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def gpt3_restaurant_review(req: Gpt3RestaurantReviewModel):
    """GPT3 model used to generate reviews of restaurants."""

    # Access openai via API key
    try:
        openai.api_key = req.apiKey

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""Write a restaurant review based on these notes:\n\n{req.prompt}\n\nReview:""",
            temperature=req.temperature,
            max_tokens=req.maxTokens,
            top_p=req.top_p,
            frequency_penalty=req.frequencyPenalty,
            presence_penalty=req.presencePenalty,
        )

        return {"Summarised text": response["choices"][0]["text"]}

    except:
        return "That didn't work. Did you provide an OpenAI API key?"
