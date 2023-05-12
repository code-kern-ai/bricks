```python
import re

def domain_parser(link:str, include_sub_domain:bool = False) -> str:
    """
    @param link: the input link
    @param include_sub_domain: Attribute whether subdomain in front of domain is desired or not
    @return: rootdomain
    """

    clean_link = re.sub("www.", "",link)
    parts = clean_link.split("/")
    domain = parts[2]
    if include_sub_domain == False:
        split = domain.split(".")
        if len(split) == 3:
            domain = str(split[1] + "." + split[2])

    return domain

# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation

def example_integration():
    links = ["https://mail.google.com/mail/u/0/?pli=1#inbox", "https://www.registry.in/internationalized-domain-names-idns", "https://www.iana.org/domains/root/db/wme.html", "https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains", "https://huggingface.co/sentence-transformers", "https://www.google.com/search?client=firefox-b-d&q=root+domain+names#imgrc=VU1Iy5dzWVXSoM","https://slack.com/intl/de-de/downloads/instructions/windows"]
    extraction_keyword = "domain"
    for link in links:
        found = domain_parser(link, False)
        if found:
            print(f"text: \"{link}\" has {extraction_keyword} -> \"{found}\"")
        else:
            print(f"text: \"{link}\" doesn't have {extraction_keyword}")

example_integration()
```