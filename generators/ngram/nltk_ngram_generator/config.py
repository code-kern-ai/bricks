from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import nltk_ngram, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=nltk_ngram,
        input_example=INPUT_EXAMPLE,
        issue_id=279,
        tabler_icon="Transform",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "ngram",
        ],  # first entry should be parent directory
        # bricks integrator information
integrator_inputs={
    "name": "nltk_ngram_generator",
    "refineryDataType": RefineryDataType.TEXT.value,
    "variables": {
        "ATTRIBUTE": {
            "selectionType": SelectionType.CHOICE.value,
            "description": "only text fields",
            "optional": "false",
            "addInfo": [
                BricksVariableType.ATTRIBUTE.value,
                BricksVariableType.GENERIC_STRING.value
            ]
        },
        "NGRAM_SIZE": {
            "selectionType": SelectionType.INTEGER.value,
            "defaultValue": 2,
            "optional": "false",
            "addInfo": [
                BricksVariableType.GENERIC_INT.value
            ]
        }
    }
}
    )
