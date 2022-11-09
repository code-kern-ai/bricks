import os
from typing import Optional
from pydantic import BaseModel

INPUT_EXAMPLE = {
    "text": "My favourite file is stored in: /usr/bin/myfavfiles/cats.png",
    "separator": None, # Use / for Linux & MacOS, use \\ for Windows. Uses os.sep otherwise
}

class PathExtractorModel(BaseModel):
    text: str
    sep: Optional[str] 

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def path_extractor(request: PathExtractorModel):
    '''Extracts paths from a given text.'''
    text = request.text
    sep = os.sep if request.sep is None else request.sep
    return [x for x in text.split() if len(x.split(sep)) > 1]