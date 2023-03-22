from util.configs import build_classifier_function_config
from util.enums import State
from . import textblob_sentiment, INPUT_EXAMPLE


def get_config():
    return build_classifier_function_config(
        function=textblob_sentiment,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=27,
        tabler_icon="MoodSmileBeam",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        type="python_function",
        inputs=[
            {
                "name": "my_text",
                "type": "text",
                "values": None,
                "example": "Wow, this is awesome!"
            }
        ],
        gdpr_compliant=True,
        kern_token_proxy_usable=False,
        docker_image="textblob_sentiment",
    )
