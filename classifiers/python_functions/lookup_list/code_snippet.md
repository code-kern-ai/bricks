```python
# the lookup list values can also come from a knowledge base, e.g.:
# from knowledge import my_lookup_list

YOUR_ATTRIBUTE = "sender"
YOUR_LOOKUP_LIST = ["johannes.hoetter@kern.ai", "henrik.wenck@kern.ai"]
YOUR_LABEL = "ham"

def lkp_known_sender(record):
    for known_sender in YOUR_LOOKUP_LIST:
        # knowledge.senders might look like this: ["johannes.hoetter@kern.ai", "henrik.wenck@kern.ai", ...]
        if known_sender.lower() in record[YOUR_ATTRIBUTE].text.lower():
            return "ham"
```