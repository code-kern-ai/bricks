from util.configs import build_classifier_function_config
from util.enums import State
from . import vader_sentiment, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        # strapi information
        function=vader_sentiment,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=157,
        tabler_icon="MoodCrazyHappy",
        min_refinery_version="1.8.0",
        state=State.PUBLIC,
        type="python_function",
        gdpr_compliant=True,
        kern_token_proxy_usable=False,
        docker_image=None,
        available_for=["refinery", "common"],
        part_of_group=["sentiment", "gdpr_compliant"],
        # bricks integrator information
        outputs=["positive" ,"neutral", "negative"],
        integrator_inputs={
            "name": "spelling_check",
            "refineryInputType": "text",
            "constants": {
                "inputRecordAttribute": {
                    "defaultValue": "text",
                    "optional": False,
                },  
                "mode": {
                    "defaultValue": "classification",
                    "classification": {
                        "type": "string",
                        "description": "Classify the sentiment as positive, neutral or negative.",
                    },
                    "scores": {
                        "type": "string",
                        "description": "Get the sentiment scores as floats.",
                    },
                },
            },
        },
    )