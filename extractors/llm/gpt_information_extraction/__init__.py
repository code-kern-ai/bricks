import openai
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiKey": "<API_KEY_GOES_HERE>",
    "text" : "The Beatles were an English rock band, formed in Liverpool in 1960, that comprised John Lennon, Paul McCartney, George Harrison and Ringo Starr.",
    "extractionKeyword": "names",
    "temperature": 0.0,
}


class GptInformationExtractionModel(BaseModel):
    apiKey: str
    text: str
    extractionKeyword: str
    temperature: float

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def gpt_information_extraction(req: GptInformationExtractionModel):
    """Uses OpenAI's GPT model to extract keyword from a text."""
    openai.api_key = req.apiKey
    try:
       response = openai.ChatCompletion.create(
           model = "gpt-3.5-turbo",
           message= [
               {
                   "role": "system",
                   "content":   f"You will extract all {req.extractionKeyword} from this text:\ {req.text} \ Return a list of json objects with the keys {req.extractionKeyword} and charPosition the {req.extractionKeyword} was found. If nothing is found return NAN!",
               },
           ],
           temperature=req.temperature,
       )
       answer = {"Extraction": response["choices"][0]["message"]["content"]}
       return {"result": answer}

    except:
        return "That didn't work! Did you provide an OpenAI API key?"
