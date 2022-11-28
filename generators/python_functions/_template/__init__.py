from pydantic import BaseModel

INPUT_EXAMPLE = {
    "text": "This is an english sentence."
    # if required, add more attributes here
}

# make sure the model name fits to the function name, as it is actually parsed
# i.e. my_gen -> MyGenModel (capitalized and "Model" appended)
class MyGenModel(BaseModel):
    text: str
    # if required, add more attributes here

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def _template(request: MyGenModel):
    """Detects the language of a given text."""

    text = request.text

    # my function logic here
    result = None

    # rename to whatever you want to call the output
    return {"generator": result}