from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import lookup_list, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=lookup_list,
        input_example=INPUT_EXAMPLE,
        issue_id=26,
        tabler_icon="ClipboardList",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",

        available_for=["refinery", "common"],
        part_of_group=[
            "lookup_lists",
        ],  # first entry should be parent directory
        # bricks integrator information
        cognition_init_mapping="none",
        integrator_inputs={
            "name": "lookup_list",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LOOKUP_LISTS": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "Either lookup lists or lookup values or both",
                    "addInfo": [
                        BricksVariableType.LOOKUP_LIST.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LOOKUP_VALUES": {
                    "selectionType": SelectionType.STRING.value,
                    "defaultValue": "john@kern.ai",
                    "optional": "true",
                    "addInfo": [BricksVariableType.GENERIC_STRING.value],
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "in lookup",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )
