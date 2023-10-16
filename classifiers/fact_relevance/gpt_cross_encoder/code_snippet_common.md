```python
import openai
import os 

openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt_cross_encoder(fact: str, question: str, api_key:str, api_base: str = "https://api.openai.com/v1", api_type: str = "open_ai", api_version: str = None, model: str = "gpt-3.5-turbo", engine: str = None, temperature: float = 0.0) -> str:
    """
    Uses OpenAIs GPT-3.5-turbo model as a cross encoder model for relevancy classification. Visit https://platform.openai.com/docs/models/gpt-3-5 for full documentation 

    @param fact: References found from a fact- or knowledge base. 
    @param question: User question for which we want to find relevant facts.
    @param api_key: OpenAI or Azure OpenAI API key.
    @param api_base: Base URL for the OpenAI API. If you are using Azure, this is the custom URL of your AZ OpenAI service.
    @param api_type: Type of the OpenAI API, either 'open_ai' or 'azure'.
    @param api_version: Version of the OpenAI API. For Azure, this can be checked here: https://learn.microsoft.com/en-us/azure/ai-services/openai/reference
    @param model: Name of the model, e.g. 'gpt-3.5-turbo', 'gpt-4 or a specific version like 'gpt-3.5-turbo-0613'.
    @param engine: Engine used for the OpenAI API. If you are using Azure, this is the custom name of your deployed model.
    @param temperature: Higher values mean the model will take more risks. E.g., 0.9 for more creative applications, and 0 for ones with a well-defined answer.
    @return: 'Yes' or 'No', depending on if the GPT models deems the found fact as relevant.
    """
    openai.api_key = api_key
    openai.api_base = api_base
    openai.api_type = api_type
    openai.api_version = api_version

    response = openai.ChatCompletion.create(
        model=model,
        engine=engine,
        messages=[
            {
                "role": "system",
                "content": f"""
                    Take a breath. You are assessing the relevance of question-fact pairs.
                    If a fact is directly related to the topic of the question (e.g. directly or even by implying consequences), it is "Relevant".
                    If there is no connection, it is "Irrelevant". In case of doubt, the fact is "Irrelevant".

                        Fact: {fact}
                        Question: {question}

                    Determine the relevance. Give a score from 0 to 100 for this (100 would be a straight answer to the question). 
                    Answer ONLY with the score itself (i.e. a number between 0 and 100).
                    If you answer with more than one number between 0 and 100, I will not process your output!""",
            },
            # {
            #     "role": "user",
            #     "content": f"Text to classify: {text}",
            # },
        ],
        temperature=temperature,
    )
    answer = response["choices"][0]["message"]["content"]

    if int(answer) > 50:
        return "Yes"
    return "No"

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    api_key = os.getenv("OPENAI_API_KEY")

    question = "I would like to learn more about the insurance policy."
    facts = [
        "Our travel insurance policy is designed to keep you save. With GlobalGuard you have strong partner - where ever you are!",
        "To make cheesecake you need Graham crackers, cream cheese, sugar, lots of butter and of course a hefty heap of love.",
        "Section A1.2 of our Global Explorer travel insurance: The insurance covers up to 100.000 EUR of damages while traveling abroad."
    ]
    
    for fact in facts:
        print(f"Is the {fact} relevant? Answer -> {gpt_cross_encoder(fact, question, api_key)}")

example_integration()
```