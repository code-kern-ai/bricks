
from pydantic import BaseModel
import dateutil.parser as dparser
import holidays

INPUT_EXAMPLE = {
    "text": "01.01.2023 is a holiday in Germany",
    "coutryCode": "DE" # optional, if not specified, it will not check for holidays
}

class WorkdayClassifierModel(BaseModel):
    text: str
    coutryCode: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def workday_classifier(req: WorkdayClassifierModel):
    """Checks if a date is a workday, weekend or a holiday."""
    text = req.text

    # try to parse the date from the string
    try:
        date = dparser.parse(text, fuzzy=True).date()
    except:
        return "No date found or invalid date"

    # check if country code is specified
    country_code = req.coutryCode
    if country_code:
        national_holidays = holidays.country_holidays(f"{country_code}")
        if date in national_holidays:
            return {"weekdayType": "Holiday"}
    
    # check if weekday is a workday or a weekend
    if date.weekday() < 5:
        return {"weekdayType": "Working day"}
    else:
        return {"weekdayType": "Weekend"}