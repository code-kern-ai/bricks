from util.configs import build_extractor_function_config
from util.enums import State
from . import email_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=email_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=23,
        tabler_icon="Mail",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        gdpr_compliant=True,
        kern_token_proxy_usable=False,
        docker_image=None,
        available_for=["refinery", "common"],
        part_of_group=["personal_identifiers", "gdpr_compliant"],
        # bricks integrator information
        outputs=["email"],
        integrator_inputs={
            "name": "email_extraction",
            "refineryInputType": "text",
            "constants": {
                "inputRecordAttribute": {
                    "defaultValue": "text",
                    "optional": False,
                },  
                "label": {
                    "defaultValue": "email",
                    "type": "string",
                    "optional": False,
                    "description": "The label you want to assign to emails.",
                },
            },
        },
    )