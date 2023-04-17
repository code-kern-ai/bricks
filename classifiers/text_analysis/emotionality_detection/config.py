from util.configs import build_classifier_function_config
from util.enums import State, RefineryDataType, SelectionType, BricksVariableType
from . import emotionality_detection, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=emotionality_detection,
        input_example=INPUT_EXAMPLE,
        issue_id=97,
        tabler_icon="MoodSad2",
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
            "name": "emotionality_detection",
            "refineryDataType": RefineryDataType.TEXT.value,
            "globalComment": "Only for english text.\nWorks best with longer texts since scores for each word are accumulated.",
            "outputs": [
                "anger",
                "fear",
                "anticipation",
                "trust",
                "surprise",
                "sadness",
                "joy",
                "disgust",
            ],
            "variables": {
                "ATTRIBUTE": {
                    "selectionType": SelectionType.CHOICE.value,
                    "addInfo": [
                        BricksVariableType.ATTRIBUTE.value,
                        BricksVariableType.GENERIC_STRING.value,
                    ],
                }
            },
        },
    )
