from fastapi import APIRouter
from .personal_identifiers import (
    address_extraction,
    email_extraction,
    person_extraction,
)

router = APIRouter()

for module in [
    address_extraction,
    email_extraction,
    person_extraction,
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
