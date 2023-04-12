from util.configs import build_classifier_function_config
from util.enums import State, BricksVariableType, RefineryDataType, SelectionType
from . import spelling_check, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        # strapi information
        function=spelling_check,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=73,
        tabler_icon="TextSpellcheck",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        gdpr_compliant="True",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=[
            "spelling",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "spelling_check",
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
                "LABEL_MISTAKES": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "contains mistakes",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LABEL_CORRECT": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "no mistakes",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )
