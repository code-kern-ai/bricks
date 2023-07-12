```python
from datetime import datetime
import holidays
import dateutil.parser as dparser
from typing import Optional

ATTRIBUTE: str = "text" # only text attributes 
COUNTRY_ID: str = "US" # optional, takes in an ISO country code, such as US, DE, UK. Leave empty if not required

def workday_classifier(record):
    text = record[ATTRIBUTE].text

    # try to parse a date from the provided string
    try:
        date = dparser.parse(text, fuzzy=True).date()
    except:
        return "Found no date, an invalid date or multiple dates."

    # check if country code is specified
    if YOUR_COUNTRY:
        national_holidays = holidays.country_holidays(f"{COUNTRY_ID}")
        if date in national_holidays:
            return "Holiday"
    
    # check if weekday is a workday or a weekend
    if date.weekday() < 5:
        return "Working day"
    else:
        return "Weekend"
```