```python
from bs4 import BeautifulSoup


def html_cleanser(text:str)->str:
    """ 
    @param text: text we check the reading time for
    @return: cleansed text
    """
    soup = BeautifulSoup(text, "html.parser")
    lines = soup.text.splitlines()
    return "\n".join([w for w in lines if len(w) >= 1])

# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["""
<!DOCTYPE html>
<html>
<body>
<h1>Website header</h1>
<p>
Hello world.
My website is live!
</p>
</body>
</html>
"""]

    for text in texts:
        print(f"the html page:{text}\nwill looked cleansed like this:\n{html_cleanser(text)}")
example_integration() 
```