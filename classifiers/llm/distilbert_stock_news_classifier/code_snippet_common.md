```python
import requests

def distilbert_stock_news_classifier(text: str, api_key: str) -> dict:
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post("https://api-inference.huggingface.co/models/KernAI/stock-news-destilbert", headers=headers, json={"inputs": text})
    json_response = response.json()
    result = [
        {item["label"]: item["score"] for item in entry}
        for entry in json_response
    ]
    return list(result[0].keys())[0]

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    api = "<API_KEY_GOES_HERE>"
    texts = [
        "Microsoft (MSFT) - Get Free Report had its price target raised to $39 from $38 by analysts at Jefferies who maintained their 'underperform' rating. In Thursday's pre-market trading session shares are advancing 1.24% to $44.79.", 
        "Unilever PLC (NYSE: UL)’s stock price has gone decline by -0.61 in comparison to its previous close of 54.27, however, the company has experienced a -1.61% decrease in its stock price over the last five trading days. The Wall Street Journal reported on 10/24/22 that Dry Shampoo Recalled Due to Potential Cancer-Causing Ingredient."
      ]
    for text in texts:
        print(f"\"{text}\" is {distilbert_stock_news_classifier(text, api)}")
example_integration()
```