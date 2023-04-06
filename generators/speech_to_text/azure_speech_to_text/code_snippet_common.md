```python
import requests

# replace this list with a list containing your data
text = ["should be path to a .wav file."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "azure_api_key": "paste your API key here.",
    "azure_resource_region": "northeurope",
    "language": "en-US",
}

def azure_speech_to_text(record):
    converted_text = []
    for entry in record["text"]:
        # first, get the .wav file and extract it's content
        wav = requests.get(entry)

        # header for the speech to text service
        headers = {
            "Ocp-Apim-Subscription-Key": record["azure_api_key"],
            "Content-Type": "audio/wav",
        }

        # set the language in the params
        params = {
            "language": record["language"],
        }

        # send out everything via a post request
        response = requests.post(
            "https://" + record["azure_resource_region"] + ".stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1",
            params=params,
            headers=headers,
            data=wav.content,
        )
        
        if response.json()["Duration"] == 0:
            print("The transcription was not successful. Did you provide a valid link to a .wav file?.")
            return None
        else:
            try:
                converted_text.append(str(response.json()["DisplayText"]))
            except:
                print("No text to display. Did you provide a valid link to a .wav file?.")
                return None
    return {"texts": converted_text}
```