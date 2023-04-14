```python
import requests

def azure_speech_to_text(link_to_wav:str, azure_api_key:str, azure_resource_region:str, language:str) -> str:
    """ Uses an Azure Speech to Text API to convert a .wav file to text.
    @param link_to_wav: The link to the .wav file.
    @param azure_api_key: The API key for the Azure Speech to Text API.
    @param azure_resource_region: The region of the Azure Speech to Text API.
    @param language: The language of the .wav file.
    @return: generated text
    """ 
    wav = requests.get(link_to_wav)
    headers = {
        "Ocp-Apim-Subscription-Key": azure_api_key,
        "Content-Type": "audio/wav",
    }
    params = {
        "language": language,
    }
    response = requests.post(
        "https://" + azure_resource_region + ".stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1",
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
# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 
def example_integration():
    links = ["should be path to a .wav file."]
    azure_api_key = "<API_KEY_TO_USE>" # paste your Azure API key here
    azure_resource_region = "northeurope"
    language = "en-US"
    
    for link in links:
        print(f"The link {link} sounds like: {azure_speech_to_text(link,azure_api_key,azure_resource_region,language)}")
example_integration() 
```