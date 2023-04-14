```python
import re
import spacy 
import itertools

# replace this list with a list containing your data
text = ["The white house is located at 1600 Pennsylvania Ave NW · 20006 Washington", "I live at 35 Wood Lane, Pilsbury ME19 7DY, United Kingdom.", "I have also lived at 221BE Baker-callum Street, London VIC 3SX, United Kingdom."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "your_text": text,
    "label": "address",
}

def address_extraction(record: dict) -> dict: 
    regex_1 = re.compile(r"(?:\d{1,5}(?:[A-Z ]+[ ]?)+(?:[A-Za-z-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr(?:\.)?|Rd(?:\.)?|Blvd(?:\.)?|Ln(?:\.)?|St(?:\.)?|Strasse|Hill|Alley|Alle|City)[,](?:[ A-Za-z0-9,]+[ ]?)?)")
    regex_2 = re.compile(r"(?:(?:[A-Za-z-]?)+[ ](?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr(?:\.)?|Rd(?:\.)?|Blvd(?:\.)?|Ln(?:\.)?|St(?:\.)?|Strasse|Str(?:\.)?|Hill|Alley|Alle|City)[ ]+\d{1,5},(?:[ A-Za-z0-9,]+[ ]?)?)")

    nlp = spacy.load("en_core_web_sm")

    address_positions = []
    text_id = 0
    for entry in record["your_text"]:  
        doc = nlp(entry)
        if regex_2.findall(entry) or regex_1.findall(entry):
            for match in itertools.chain(regex_1.finditer(entry), regex_2.finditer(entry)):
                start, end = match.span()
                span = doc.char_span(start, end, alignment_mode="expand")
                address_positions.append({f"text_{text_id}" :[record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": address_positions}
```