# content-library-endpoints
Code for the deployment of content library endpoints. These are _only_ the endpoints, i.e. if an endpoint is added here, it isn't directly available in the content library, which is managed via a Strapi backend.

## Calling endpoints
The endpoints are available at route `/docs`. On your local machine, you can run e.g. `localhost:8000/docs`.

## Different types of endpoints
Generally, there are four types of endpoints:

- Python functions
- Active learning configurations
- Zero shot configurations
- Pre-trained models

See in each subsection how to add them to the content library.

### Python functions
- **Maintain source code in Strapi**
- **Available as endpoint**

For instance to detect languages in texts via existing libraries, such as the language detection endpoint:
```python
from pydantic import BaseModel
from langdetect import detect, DetectorFactory 
DetectorFactory.seed = 0

class LanguageDetectionModel(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "This is an english sentence."
            }
        }


def fn_language_detection(request: LanguageDetectionModel):
    """Detect language of text
        
    Args:
        request (LanguageDetectionModel): schema of request body

    Returns:
        dict: Language of text
    """

    text = request.text
    language = detect(text)
    return {"language": language}
```

Which is available as a `POST` endpoint at `/classifiers/language_detection/`.

They are available as endpoints in the playground, i.e. you can just call them right away with your inputs. Users of the content library however should be able to modify this code. Hence, when importing the module from the library, they have access to the direct source code instead of a request to an endpoint. This source code is maintained in Strapi. 

#### Source code structure
_The source code differs from the one used in the endpoint w.r.t. structure!_ For instance, above listed endpoint would look as follows in Strapi:
```python
from typing import Dict, Any
from langdetect import detect

def fn_language_detection(record: Dict[str, Any]) -> str:
    """Detect language of text
        
    Args:
        record (Dict): one single record you want to process

    Returns:
        str: Language of your text
    """

    text = record["your-text"]
    language = detect(text)
    return language

```

### Active learning configurations
- **Maintain source code in Strapi**
- **Not available as endpoint**

Active learning implies that the module needs access to the labeled training data of the project. For that reason, active learning can't be executed in the playground. All configurations for active learning are maintained in Strapi.

### Zero shot configurations
- **Maintain source code in Strapi**
- **Available as endpoint**

Zero shot modules will be callable from the playground, and for that reason will also have some endpoints in this repository.

Currently, we don't have programmable zero shot modules. When we'll add a programming interface for zero shot, we'll look into these configurations further.

### Pre-trained models and 3rd party providers
- **Closed source**
- **Available as endpoint**

We will offer "premium" endpoints, which can be accessed only via the endpoint (i.e. the source code is not available). This is either because the module calls a paid 3rd-party, or because the module uses a proprietary model maintained by Kern AI.

## Contributing new endpoints
To add a new endpoint, please open a dedicated pull request containing _only_ this one endpoint. Each endpoint should have a dedicated file, such that merging should become trivial if done correctly.