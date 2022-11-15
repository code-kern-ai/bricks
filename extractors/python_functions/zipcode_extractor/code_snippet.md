```python
zip_codes ={
    "US": r"\d{5}([ \-]\d{4})?",
    "CA": r"[ABCEGHJKLMNPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ ]?\d[ABCEGHJ-NPRSTV-Z]\d",
    "DE": r"\d{5}"
}

YOUR_ATTRIBUTE = "text"
COUNTRY_ID = "US" # Or CA, DE. Visit GitHub for extensive list of country zip-codes

def zipcode_extractor(record):
    country_id = COUNTRY_ID
    text = record[YOUR_ATTRIBUTE].text

    match = re.search(zip_codes_json[country_id], text)

    start, end = match.span()
    span = record[YOUR_ATTRIBUTE].char_span(start, end, alignment_mode="expand")

    yield f"{country_id} zip code", span.start, span.end
```