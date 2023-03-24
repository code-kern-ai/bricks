from util.configs import build_generator_function_config
from util.enums import State
from . import euclidean_distance, INPUT_EXAMPLE


def get_config():
    return build_generator_function_config(
        function=euclidean_distance,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=230,
        tabler_icon="VectorTriangle",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        gdpr_compliant=True,
        kern_token_proxy_usable=False,
        docker_image=None,
        available_for=["refinery", "common"],
        part_of_group=["distance", "gdpr_compliant"],
        # bricks integrator information
        outputs=["contains mistakes", "no mistakes"],
        integrator_inputs={
            "name": "spelling_check",
            "refineryInputType": "text",
            "constants": {
                "inputRecordAttribute": {
                    "defaultValue": "text",
                    "optional": False,
                },  
                "subjectText": {
                    "defaultValue": "The sun is not made out of pancakes.",
                    "type": "string",
                    "optional": False,
                    "description": "The text you want to compare your records to.",
                },
            },
        },
    )