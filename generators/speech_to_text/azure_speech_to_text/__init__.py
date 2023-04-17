from pydantic import BaseModel
import requests

INPUT_EXAMPLE = {
    "urlToFile": "https://drive.google.com/uc?export=download&id=10TWBH4NuR3KNG4MWpuY1XxOLcGRGZSeC",
    "apiKey": "<API_KEY_GOES_HERE>",
    "region": "northeurope",
    "language": "en-US",
}


class AzureSpeechToTextModel(BaseModel):
    urlToFile: str
    apiKey: str
    region: str
    language: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def azure_speech_to_text(req: AzureSpeechToTextModel):
    """Transcribes a .wav file to text using Azure Speech-to-Text."""

    wav = requests.get(req.urlToFile)

    headers = {
        "Ocp-Apim-Subscription-Key": req.apiKey,
        "Content-Type": "audio/wav",
    }

    params = {
        "language": req.language,
    }

    response = requests.post(
        "https://"
        + req.region
        + ".stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1",
        params=params,
        headers=headers,
        data=wav.content,
    )

    if response.json()["Duration"] == 0:
        return {
            "transcription": "The transcription was not successful. Did you provide a valid link to a .wav file?."
        }
    else:
        try:
            return {"transcription": response.json()["DisplayText"]}
        except:
            return {
                "transcription": "No text to display. Did you provide a valid link to a .wav file?."
            }
