```python
import requests

YOUR_ATTRIBUTE: str = "url" # only text attributes. Keep in mind that this requires you to have a downloadable link in your attribute field
YOUR_API_KEY: str = "<you-api-key-here>"
YOUR_RESOURCE_REGION: str = "northeurope" # region where your resource is deployed
YOUR_LANGUAGE: str = "en-US" 

def azure_speech_to_text(record):

    # first, get the .wav file and extract it's content
    wav = requests.get(record[YOUR_ATTRIBUTE].text)
    wav_content = wav.content

    # header for the speech to text service
    headers = {
        "Ocp-Apim-Subscription-Key": YOUR_API_KEY,
        "Content-Type": "audio/wav",
    }

    # set the language in the params
    params = {
        "language": YOUR_LANGUAGE,
    }

    # send out everything via a post request
    response = requests.post(
        "https://" + YOUR_RESOURCE_REGION+ ".stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1",
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