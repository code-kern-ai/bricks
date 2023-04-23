```python
import textstat

# replace this list with a list containing your data
text = ["Pizza is very delicious.", "Titanic is a movie made by James Cameron", "Apple pie is also very delicious."]

# add the texts to a dict called records. Add further information as key-value pairs if needed
record = {
    "text": text,
}

def reading_time(record):
    time_list = []
    for entry in record["text"]:
        time_list.append(textstat.reading_time(entry, ms_per_char=14.69))
    return {"readingTimes": time_list}
```