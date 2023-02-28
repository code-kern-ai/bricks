import requests
import json

from pydantic import BaseModel

INPUT_EXAMPLE = {
    "url":  "https://kern-assets.s3.eu-central-1.amazonaws.com/dev/Aufzeichnung.wav",
    "apiKey": "<YOUR_KEY_HERE>", 
}

class OpenaiWhisperModel(BaseModel):
    url: str 
    apiKey: str 

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}

def openai_whisper(req: OpenaiWhisperModel):
    """Takes in a url to an audio-file and returns the text transcription of the audio file."""

    headers = {
        "Authorization": f"Api-Key {req.apiKey}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "url": req.url,
    }

    response = requests.post("https://app.baseten.co/model_versions/qjdelgq/predict", headers=headers, data=json.dumps(data))

    return {"transcription": str(response.json()["model_output"]["text"])}