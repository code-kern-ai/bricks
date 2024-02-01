```python

import requests

def emotionality_detection(text, api_key):
      headers = {"Authorization": f"Bearer {api_key}"}
      data = {"inputs": text}
      try: 
            response = requests.post("https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base", headers=headers, json=data)
            response_json = response.json()

            # flatten the list of lists
            flat_list = [item for sublist in response_json for item in sublist]

            # find the item with the highest score
            max_item = max(flat_list, key=lambda x: x["score"])

            # retrieve the label of the item with the highest score
            max_label = max_item["label"]

            return max_label
      except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response_json}"

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
      hf_api_key = "<API_KEY_GOES_HERE>"
      texts = ["What a great day to go to the beach.", "Sorry to hear that. CAn I help you?", "Why the hell would you do that?"]
      for text in texts:
            output = emotionality_detection(text, api_key=hf_api_key)
            print(output)

example_integration()
```