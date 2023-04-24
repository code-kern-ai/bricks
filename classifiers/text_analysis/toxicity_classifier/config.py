from util.configs import build_classifier_premium_config
from util.enums import State, SelectionType, BricksVariableType, RefineryDataType
from . import toxicity_classifier, INPUT_EXAMPLE


def get_config():
    return build_classifier_premium_config(
        function=toxicity_classifier,
        input_example=INPUT_EXAMPLE,
        issue_id=80,
        tabler_icon="MoodAngry",
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
