```python
from quantulum3 import parser

# replace this list with a list containing your data
text = ["My weight is 82 kilos. The eifel tower is 187 meters high."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
    "label": "metric",
}

def metric_extraction(record):
    metric_positions = []
    text_id = 0
    for entry in record["text"]:
        quants = parser.parse(entry)
        for quant in quants:
            span = quant.span
            metric_positions.append({f"text_{text_id}": [record["label"], span[0], span[1]]})
        text_id += 1
    return {"extractions": metric_positions}
```