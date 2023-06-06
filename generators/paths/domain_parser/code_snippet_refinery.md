```python
from urllib.parse import urlsplit

ATTRIBUTE: str = "text" # only text attributes

def domain_parser(record):
    link = record[ATTRIBUTE].text
    if "http" in link:
        parser = urlsplit(link)
        domain = parser.netloc
    else:
        part = link.strip('/').split('/')
        domain = part[0]
    if "www." in domain:
            domain = domain.lstrip("www.")
    return domain

```
