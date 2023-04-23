```python
import requests

ATTRIBUTE: str = "url" # only text attributes
API_KEY: str = "<you-api-key-here>"
RESOURCE_REGION: str = "northeurope" # region where your resource is deployed
LANGUAGE: str = "en-US" 

def azure_speech_to_text(record):
    wav = requests.get(record[ATTRIBUTE].text)
    wav_content = wav.content

    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "audio/wav",
    }
    params = {
        "language": LANGUAGE,
    }
    response = requests.post(
        "https://" + RESOURCE_REGION+ ".stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1",
        params=params,
        headers=headers,
        data=wav.content,
    )
    
    if response.json()["Duration"] == 0:
        print("The transcription was not successful. Did you provide a valid link to a .wav file?.")
        return None
    else:
        try:
            return str(response.json()["DisplayText"])
        except:
            print("No text to display. Did you provide a valid link to a .wav file?.")
            return None
```