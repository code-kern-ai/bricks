from pydantic import BaseModel
from quantulum3 import parser

INPUT_EXAMPLE = {
    "text": "My weight is 82 kilos. The eifel tower is 187 meters high.",
}

class MetricDetectionModel(BaseModel):
    text: str

    class Config:
        schema_extra = {"example": INPUT_EXAMPLE}

def metric_detection(request: MetricDetectionModel):
    """Extracts units of measurement from a string."""
    text = request.text
    
    quants = parser.parse(text)
    units = []
    for quant in quants:
        span = quant.span
        name = quant.unit.name

        units.append([name, span[0], span[1]])

    return {"metric": units}
