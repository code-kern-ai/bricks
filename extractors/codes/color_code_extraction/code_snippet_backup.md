```python
import re
import spacy

# replace this list with a list containing your data
text = ["One of our corporate colors is #75EA8E.", "The color code of white is #FFFFFF."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "color",
}

nlp = spacy.load("en_core_web_sm")

def color_code_extraction(record):
    color_code_positions = []
    text_id = 0
    for entry in record["text"]:
        doc = nlp(entry)

        hexcolor_regex = re.compile(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})(?![0-9a-fA-F])")
        rgb_regex = re.compile(r"(rgba|rgb)\([^\)]*\)")
        hsl_regex = re.compile(r"(hsla|hsl)\([^\)]*\)")
        hwb_regex = re.compile(r"hwb\([^\)]*\)")

        for regex in [hexcolor_regex, rgb_regex, hsl_regex, hwb_regex]:
            for match in regex.finditer(entry):
                start, end = match.span()
                span = doc.char_span(start, end, alignment_mode="expand")
                color_code_positions.append({f"text_{text_id}": [record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": color_code_positions}
```