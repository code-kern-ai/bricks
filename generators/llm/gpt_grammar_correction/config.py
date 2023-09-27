from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import gpt_grammar_correction, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=gpt_grammar_correction,
        input_example=INPUT_EXAMPLE,
        issue_id=190,
        tabler_icon="Checks",
        min_refinery_version="1.8.0",
        state=State.PUBLIC.value,
        type="python_function",

        available_for=["refinery", "common"],
        part_of_group=[
            "llm",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping=None,
        integrator_inputs={
            "name": "gpt_grammar_correction",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "API_KEY": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "TEMPERATURE": {
                    "selectionType": SelectionType.RANGE.value,
                    "defaultValue": 0,
                    "allowedValueRange": [0, 100],
                    "addInfo": [BricksVariableType.GENERIC_FLOAT.value],
                },
            },
        },
    )
