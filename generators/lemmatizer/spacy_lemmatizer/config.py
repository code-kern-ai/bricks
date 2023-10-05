from util.configs import build_generator_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import spacy_lemmatizer, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=spacy_lemmatizer,
        input_example=INPUT_EXAMPLE,
        issue_id=228,
        tabler_icon="Transform",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        available_for=["refinery", "common"],
        part_of_group=[
            "lemmatizer",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "spacy_lemmatizer",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                }
            },
        },
    )
