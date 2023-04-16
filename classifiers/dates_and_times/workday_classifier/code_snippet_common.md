```python
from datetime import datetime
import holidays
import dateutil.parser as dparser
from typing import Optional

def workday_classifier(text: str, country_id: str) -> str:
    # try to parse a date from the provided string
    try:
        date = dparser.parse(text, fuzzy=True).date()
    except:
        return "Found no date, an invalid date or multiple dates."

    # check if country code is specified
    if country_id:
        national_holidays = holidays.country_holidays(f"{country_id}")
        if date in national_holidays:
            return "Holiday"
    
    # check if weekday is a workday or a weekend
    if date.weekday() < 5:
        return "Working day"
    else:
        return "Weekend"
    
# ↑ necessary bricks function 
# -----------------------------------------------------------------------------------------
# ↓ example implementation 

def example_integration():
    texts = ["01.01.2023 is a holiday in Germany", "02.01.2023 is not a holiday"]
    country_id = "DE"
    
    for text in texts:
        found = workday_classifier(text, country_id)
        if found == "Holiday":
            print(f"text: \"{text}\" is a holiday")
        else:
            print(f"text: \"{text}\" is a working day")

example_integration()
```