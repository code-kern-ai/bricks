```python
# replace this list with a list containing your data
texts = ["Please contact john@kern.ai to get more info.", "This is a negative text."]
lookup_values = ["john@kern.ai", "jane@kern.ai"]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": texts,
    "lookup_list": lookup_values,
    "label": "mail",
}

def lookup_list(record):
    labels, text_id = [], 0
    for item in record["lookup_list"]:
        for entry in record["text"]:
            if item.lower() in entry: 
                labels.append([record["label"], text_id])
        text_id += 1
    return {"lookup_labels": labels}
```