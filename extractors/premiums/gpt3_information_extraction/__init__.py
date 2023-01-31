import openai
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiKey": "<API_KEY_GOES_HERE>",
    "prompt": "The Beatles were an English rock band, formed in Liverpool in 1960, that comprised John Lennon, Paul McCartney, George Harrison and Ringo Starr.",
    "extractionKeyword": "names",
    "temperature": 0.0,
    "maxTokens": 64,
    "top_p": 1.0,
    "frequencyPenalty": 0.0, 
    "presencePenalty": 0.0
}

class Gpt3InformationExtractionModel(BaseModel):
    apiKey: str
    prompt: str
    extractionKeyword: str
    temperature: float
    maxTokens: int
    top_p: float
    frequencyPenalty: float
    presencePenalty: float

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}

def gpt3_information_extraction(req: Gpt3InformationExtractionModel):
    '''Uses OpenAI's GPT-3 model to extract keyword from a text.'''
    # Access openai via API key
    try: 
        openai.api_key = req.apiKey

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""
                Extract all {req.extractionKeyword} from this sentence:\n\n
                {req.prompt}""",
            temperature=req.temperature,
            max_tokens=req.maxTokens,
            top_p=req.top_p,
            frequency_penalty=req.frequencyPenalty,
            presence_penalty=req.presencePenalty
        )

        return {"Extraction": response["choices"][0]["text"]}
    
    except: 
        return "That didn't work. Did you provide an OpenAI API key?"