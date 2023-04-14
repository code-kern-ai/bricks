```python
import re
import spacy

# replace this list with a list containing your data
text = ["Today is 04.11.2022. Yesterday was 03/11/2022.", "Tomorrow is 05-11-2022. Day after tomorrow is 6 Nov 2022.",]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "date",
}

def date_extraction(record):
    regex = re.compile(
        r"(?:[0-9]{1,2}|[0-9]{4}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[\/\. -]{1}(?:[0-9]{1,2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[,\/\. -]{1}(?:[0-9]{2,4})"
    )
    nlp = spacy.load("en_core_web_sm")

    date_positions = []
    text_id = 0
    for entry in record["text"]:#
        doc = nlp(entry)
        for match in regex.finditer(entry):
            start, end = match.span()
            span = doc.char_span(start, end, alignment_mode="expand")
            date_positions.append({f"text_{text_id}" :[record["label"], span.start, span.end]})
        text_id += 1
    return {"extraction": date_positions}
```