import requests
import json
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "apiToken": "<API_KEY_GOES_HERE>",
    "text": "Microsoft (MSFT) - Get Free Report had its price target raised to $39 from $38 by analysts at Jefferies who maintained their 'underperform' rating. In Thursday's pre-market trading session shares are advancing 1.24% to $44.79."
}

class DistilbertStockNewsClassifierModel(BaseModel):
    apiToken: str
    text: str

    class Config:
        schema_example = {"example": INPUT_EXAMPLE}


def distilbert_stock_news_classifier(req: DistilbertStockNewsClassifierModel):
    """Uses the Hugging Face API to classify text as toxic or not toxic."""
    def query(api_token, inputs):
        headers = {"Authorization": f"Bearer {api_token}"}
        response = requests.post("https://api-inference.huggingface.co/models/KernAI/stock-news-destilbert", headers=headers, json={"inputs": inputs})
        json_response = response.json()
        result = [
            {item["label"]: item["score"] for item in entry}
            for entry in json_response
        ]
        return str(list(result[0].keys())[0])

    try:
        output = query(req.apiToken, req.text)
        return output
    except Exception as e:
        return f"That didn't work. Did you provide a valid Hugging Face API key? Got error {e}"