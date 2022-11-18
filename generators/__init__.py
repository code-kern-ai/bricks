from fastapi import APIRouter
from .python_functions import (
    language_translator
)
from .premium import (
    microsoft_translator,
    deepl_translator
)

router = APIRouter()

for module in [
    language_translator,
    microsoft_translator,
    deepl_translator
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