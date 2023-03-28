from util.configs import build_classifier_function_config
from util.enums import State
from . import textblob_sentiment, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        # strapi information
        function=textblob_sentiment,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=27,
        tabler_icon="MoodSmileBeam",
        min_refinery_version="1.7.0",
        state=State.PUBLIC.value,
        type="python_function",
        gdpr_compliant="True",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["sentiment", "gdpr_compliant"],
        # bricks integrator information
        integrator_inputs={
            "name": "textblob_sentiment",
            "refineryInputType": "text",
            "possibleOutputs": ["very positive", "positive" ,"neutral", "negative", "very negative"],
            "constants": {
                "inputAttribute": { # previously YOUR_ATTRIBUTE, never optional
                    "selectionType": "string",
                    "defaultValue": "your-text",
                },  
                "minScore": {
                    "selectionType": "range",
                    "defaultValue": -100,
                    "allowedValueRange": [-100, 0], # from -100 to 0
                    "description": "The lowest possible sentiment score.",
                    "optional": "False",
                },
                "maxScore": {
                    "selectionType": "range",
                    "defaultValue": 100,
                    "allowedValueRange": [1, 100], # from 1 to 100
                    "description": "The highest possible sentiment score.",
                    "optional": "False",
                },
            },
        },
    )
