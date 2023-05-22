```python
import re

ATTRIBUTE: str = "text" # only text attributes
LABEL: str = "domain"
SUBLABEL: str = "False" #"True"

def domain_parser(record):
    text = record[ATTRIBUTE].text

    clean_link = re.sub("www.", "",text)
    parts = clean_link.split("/")
    domain = parts[2]
    if SUBLABEL == False:
        split = domain.split(".")
        if len(split) == 3:
            domain = str(split[1] + "." + split[2])

    return domain

```
