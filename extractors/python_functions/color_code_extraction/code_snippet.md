```python
def my_tagger(record):
    text = record["text-attribute"].text

    hexcolor_regex = re.compile(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})(?![0-9a-fA-F])")
    rgb_regex = re.compile(r"(rgba|rgb)\([^\)]*\)")
    hsl_regex = re.compile(r"(hsla|hsl)\([^\)]*\)")
    hwb_regex = re.compile(r"hwb\([^\)]*\)")

    color_codes = []
    for regex in [hexcolor_regex, rgb_regex, hsl_regex, hwb_regex]:
        for match in regex.finditer(text):
            start, end = match.span()
            span = doc.char_span(start, end)
            yield "color", span.start, span.end 
```