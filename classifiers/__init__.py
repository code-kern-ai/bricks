from fastapi import APIRouter
from .sentiment import (
    textblob_sentiment,
    vader_sentiment,
)

from .spelling import (
    spelling_check,
)

router = APIRouter()

for module in [
    textblob_sentiment,
    spelling_check,
    vader_sentiment,
]:
    module_name = module.__name__.split(".")[-1]
    model_name = (
        "".join([term.capitalize() for term in module_name.split("_")]) + "Model"
    )
    exec(
        f"""
@router.post("/{module_name}")
async def api_{module_name}(request: {module_name}.{model_name}):
    return {module_name}.{module_name}(request)
    """
    )
