from fastapi import APIRouter
from .python_functions import (
    language_translator,
    html_cleanser
)

router = APIRouter()

for module in [
    language_translator,
    html_cleanser
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