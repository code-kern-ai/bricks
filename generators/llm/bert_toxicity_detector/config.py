from util.configs import build_generator_premium_config
from util.enums import State, SelectionType, BricksVariableType, RefineryDataType
from . import bert_toxicity_detector, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=bert_toxicity_detector,
        input_example=INPUT_EXAMPLE,
        issue_id=80,
        tabler_icon="MoodAngry",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="premium",

        available_for=["refinery", "common"],
        part_of_group=[
            "llm",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping=None,
        integrator_inputs={
            "name": "toxicity_classifier",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "API_KEY": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
            }
        }
    )
