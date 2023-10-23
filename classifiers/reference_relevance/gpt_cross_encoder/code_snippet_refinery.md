```python
import openai

QUESTION: str = "question" # only text attributes
REFERENCE: str = "reference" # only text attributes
API_KEY: str = "<API_KEY_GOES_HERE>"
API_BASE: str = "https://api.openai.com/v1" # Optional: Unique URL of your Azure OpenAI service.
API_TYPE: str = "open_ai" # Optional: Use 'azure' if you are using the Azure service.
API_VERSION: str = None # Optional: Only needed when using the Azure service. Current version can be checked here: https://learn.microsoft.com/en-us/azure/ai-services/openai/reference
ENGINE: str = None # Optional: Only needed when using the Azure service. With Azure, this is the unique deployment name of your model.
TEMPERATURE: float = 0.0

openai.api_key = API_KEY
openai.api_base = API_BASE
openai.api_type = API_TYPE
openai.api_version = API_VERSION

def gpt_cross_encoder(record):
    try:
        score = gpt_relevance_score(record)
    except Exception as e:
        print(f"Run into the following error: {e}. No classification.")
        return

    if score > 50:
        return "Yes"
    return "No"

def gpt_relevance_score(record):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        engine=ENGINE,
        messages=[
            {
                "role": "system",
                "content": f"""
                    Take a breath. You are assessing the relevance of question-reference pairs.
                    If a reference is directly related to the topic of the question (e.g. directly or even by implying consequences), it is "Relevant".
                    If there is no connection, it is "Irrelevant". In case of doubt, the reference is "Irrelevant".

                        Reference: {record[REFERENCE].text}
                        Question: {record[QUESTION].text}

                    Determine the relevance. Give a score from 0 to 100 for this (100 would be a straight answer to the question).
                    Answer ONLY with the score itself (i.e. a number between 0 and 100).
                    If you answer with more than one number between 0 and 100, I will not process your output!""",
            },
        ],
        temperature=TEMPERATURE,
    )
    return int(response["choices"][0]["message"]["content"])
```
