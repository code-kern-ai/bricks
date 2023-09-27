from util.configs import build_extractor_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import gazetteer_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=gazetteer_extraction,
        input_example=INPUT_EXAMPLE,
        issue_id=31,
        tabler_icon="Affiliate",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",

        available_for=["refinery", "common"],
        part_of_group=[
            "functions",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping="none",
        integrator_inputs={
            "name": "gazetteer_extraction",
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
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "PERSON",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LOOKUP_LISTS": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "either lookup lists or lookup values or both",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LOOKUP_LIST.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LOOKUP_VALUES": {
                    "selectionType": SelectionType.LIST.value,
                    "defaultValue": "Max",
                    "optional": "false",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
            },
        },
    )
