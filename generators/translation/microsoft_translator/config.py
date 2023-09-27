from util.configs import build_generator_premium_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import microsoft_translator, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=microsoft_translator,
        input_example=INPUT_EXAMPLE,
        issue_id=115,
        tabler_icon="BrandWindows",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="premium",

        available_for=["refinery", "common"],
        part_of_group=[
            "translation",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping="none",
        integrator_inputs={
            "name": "microsoft_translator",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "API_KEY": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "<API_KEY_GOES_HERE>",
                    "description": "Microsoft API key",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "ORIGINAL_LANGUAGE": {
                    "selectionType": SelectionType.STRING.value,
                    "description": "only iso format",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value,
                        BricksVariableType.LANGUAGE.value,
                    ],
                },
                "TARGET_LANGUAGE": {
                    "selectionType": SelectionType.STRING.value,
                    "description": "only iso format",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value,
                        BricksVariableType.LANGUAGE.value,
                    ],
                },
            },
        },
    )
