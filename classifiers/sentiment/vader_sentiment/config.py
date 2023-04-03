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
        state=State.PUBLIC.value,
        type="python_function",
        gdpr_compliant="True",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["sentiment", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "globalComment": "Only for english text.",
            "name": "vader_sentiment",
            "refineryDataType": "text",
            "outputs": ["positive" ,"neutral", "negative"],
            "constants": {
                "inputAttribute": { # previously YOUR_ATTRIBUTE, never optional
                    "selectionType": "string",
                    "defaultValue": "your-text",
                    "addInfo": [] # enum for only text etc or additional information 
                },  
                "mode": {
                    "selectionType": "choice", # should be enum
                    "allowedValues": ["classification", "scores"],
                    "defaultValue": "classification",
                    "description": "Choose classification to return either positive, neutral or negative. Choose scores to retrieve a float score.",
                    "optional": "False", # should be enum
                },
            },
        },
    )