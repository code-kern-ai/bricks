```python
from urllib.parse import urlsplit

def domain_parser(link:str) -> str:
    if "http" in link:
        parser = urlsplit(link)
        domain = parser.netloc
    else:
        part = link.strip('/').split('/')
        domain = part[0]
    if "www." in domain:
            domain = domain.lstrip("www.")
    return domain

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    links = ["linkedin.com", "www.linkedin.com/mynetwork/epic", "www.linkedin.com", "https://mail.google.com/mail/u/0/?pli=1#inbox", "https://www.registry.in/internationalized-domain-names-idns", "https://www.iana.org/domains/root/db/wme.html", "https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains", "https://huggingface.co/sentence-transformers", "https://www.google.com/search?client=firefox-b-d&q=root+domain+names#imgrc=VU1Iy5dzWVXSoM","https://slack.com/intl/de-de/downloads/instructions/windows"]
    extraction_keyword = "domain"
    for link in links:
        found = domain_parser(link, False)
        if found:
            print(f"text: \"{link}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{link}\" doesn't have {extraction_keyword}")

example_integration()
```