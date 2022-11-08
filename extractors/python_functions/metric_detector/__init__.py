from pydantic import BaseModel
from quantulum3 import parser

INPUT_EXAMPLE = {
    "text": "My weight is 82 kilos. The eifel tower is 187 meters high.",
}


class MetricDetectorModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}


def metric_detector(request: MetricDetectorModel):
    """Detects metric values in a text, e.g. kilos, meters, etc."""
    text = request.text
    quants = parser.parse(text)
    return {"metrics": quants}
