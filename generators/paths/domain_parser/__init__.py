from pydantic import BaseModel
from urllib.parse import urlsplit

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
    if "http" in link:
        parser = urlsplit(link)
        domain = parser.netloc
    else:
        part = link.strip('/').split('/')
        domain = part[0]
    if "www." in domain:
            domain = domain.lstrip("www.")
    return domain



