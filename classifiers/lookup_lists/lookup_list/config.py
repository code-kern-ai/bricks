from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import lookup_list, INPUT_EXAMPLE

def get_config():
    return build_classifier_function_config(
        function=lookup_list,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=26,
        tabler_icon="ClipboardList",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["lookup_lists", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "lkp_known_sender",
            "refineryDataType": RefineryDataType.TEXT.value,
            "globalComment": "the lookup list values can also come from a knowledge base, e.g.:\nfrom knowledge import my_lookup_list\nIf further values are specified, add them to the lookup list.",
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "LOOKUP_LIST": {
                    "selectionType": SelectionType.CHOICE.value,
                    "description": "Change this to the name of your lookup list",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LOOKUP_LIST.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "LOOKUP_VALUES": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "john@kern.ai",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "LABEL": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "ham",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.GENERIC_STRING.value
                    ]
                }
            }
        }
    )
