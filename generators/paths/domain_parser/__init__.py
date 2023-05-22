from pydantic import BaseModel
import re

INPUT_EXAMPLE = {
    "text": "https://huggingface.co/sentence-transformers",
}

class DomainParserModel(BaseModel):
    text: str
    subdomain : bool

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def domain_parser(request: DomainParserModel):
    link = request.text
    include_sub_domain = request.subdomain

    clean_link = re.sub("www.", "",link)
    parts = clean_link.split("/")
    domain = parts[2]
    if include_sub_domain == False:
        split = domain.split(".")
        if len(split) == 3:
            domain = str(split[1] + "." + split[2])

    return domain



