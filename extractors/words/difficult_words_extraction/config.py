from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, SelectionType, BricksVariableType
from . import difficult_words_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=difficult_words_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=227,
        state=State.PUBLIC.value,
        type="python_function",
        min_refinery_version="1.8.0",
        tabler_icon="TextOrientation",
        available_for=["refinery", "common"],
        part_of_group=[
            "words",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "difficult_words_extraction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "SYLLABLE_THRESHOLD": {
                    "selectionType": SelectionType.INTEGER.value,
                    "defaultValue": 3,
                    "allowedValueRange": [1, 100],
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_INT.value],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "keyword",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )
