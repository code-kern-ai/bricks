```python
import html

def html_unescape(text:str):
    """ 
    @param text: text we to unescape
    @return: unescaped text
    """
    unescaped_text = html.unescape(text)
    return unescaped_text


# ↑ necessary bricks stuff
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["""Here&#39;s how &quot;Kern.ai Newsletter&quot; did today. 3. "World&#8217;s largest tech conference: &quot;Innovate 2023&#8482;&quot; begins tomorrow!"""]

    for text in texts:
        print(f"the html page:{text}\nwill looked unescaped like this:\n{html_unescape(text)}")
example_integration() 
```