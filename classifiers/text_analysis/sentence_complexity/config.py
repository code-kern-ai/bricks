from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, BricksVariableType, SelectionType
from . import sentence_complexity, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=sentence_complexity,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=2,
        tabler_icon="Abacus",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["distance", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "sentence_complexity",
            "refineryDataType": RefineryDataType.TEXT.value,
            "outputs": [
                "very easy",
                "easy",
                "fairly easy",
                "standard",
                "fairly difficult",
                "difficult",
                "very difficult"
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value
                    ]
                },
                "TARGET_LANGUAGE": {
                    "selectionType": SelectionType.STRING.value,
                    "description": "iso codes",
                    "optional": "false",
                    "addInfo": [
                        BricksVariableType.LANGUAGE.value
                    ]
                }
            }
        }
    )
