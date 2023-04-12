from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import profanity_detection, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=profanity_detection,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=-128,
        tabler_icon="MoodWrrr",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        gdpr_compliant="true",
        type="python_function",
        kern_token_proxy_usable="false",
        docker_image="none",
        available_for=["refinery", "common"],
        part_of_group=[
            "text_analysis",
            "gdpr_compliant",
        ],  # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "profanity_detection",
            "refineryDataType": RefineryDataType.TEXT.value,
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LABEL_PROFANE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "profane",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
                "LABEL_NOT_PROFANE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "defaultValue": "not_profane",
                    "addInfo": [
                        BricksVariableType.LABEL.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                },
            },
        },
    )
