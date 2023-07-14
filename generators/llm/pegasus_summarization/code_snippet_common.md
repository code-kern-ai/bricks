```python
import requests

def pegasus_summarization(text, api_key):
      headers = {"Authorization": f"Bearer {api_key}"}
      data = {"inputs": text, "options": {"wait_for_model": "true"}}
      try:
            response = requests.post("https://api-inference.huggingface.co/models/google/pegasus-large", headers=headers, json=data)
            response_json = response.json()

            return response_json[0]["summary_text"]
      except Exception as e: 
            return f"That didn't work. Did you provide a valid API key? Go error: {e} and message: {response_json}"

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
      hf_api_key = "<API_KEY_GOES_HERE>"
      text = ["The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."]
      output = pegasus_summarization(text, api_key=hf_api_key)
      print(f"text with length of {len(text)} chars was reduced to the text \n -> {output}")

example_integration()
```