from fastapi import APIRouter
from .distance import (
    hamming_distance,
    levenshtein_distance,
    euclidean_distance,
)

from .translation import (
    deepl_translator,
    ibm_translator,
    language_translator,
    microsoft_translator,
)

router = APIRouter()

for module in [
    language_translator,
    microsoft_translator,
    deepl_translator,
    hamming_distance,
    levenshtein_distance,
    ibm_translator,
    euclidean_distance,
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