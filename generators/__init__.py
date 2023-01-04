from fastapi import APIRouter
from .python_functions import (
    language_translator,
    html_cleanser,
    soundex_generator,
    spelling_correction,
    smalltalk_truncation,
)
from .premiums import (
    microsoft_translator,
    deepl_translator,
    ibm_translator,
    gpt3_grammar_correction,
    gpt3_tldr_summarization,
)

router = APIRouter()

for module in [
    language_translator,
    html_cleanser,
    microsoft_translator,
    deepl_translator,
    soundex_generator,
    spelling_correction,
    smalltalk_truncation,
    ibm_translator,
    gpt3_grammar_correction,
    gpt3_tldr_summarization,
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