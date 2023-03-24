from util.configs import build_extractor_function_config
from util.enums import State
from . import person_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=person_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=34,
        tabler_icon="User",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        gdpr_compliant=True,
        kern_token_proxy_usable=False,
        docker_image=None,
        available_for=["refinery", "common"],
        part_of_group=["personal_identifiers", "gdpr_compliant"],
        # bricks integrator information
        outputs=["name"],
        integrator_inputs={
            "name": "person_extraction",
            "refineryInputType": "text",
            "constants": {
                "inputRecordAttribute": {
                    "defaultValue": "text",
                    "optional": False,
                },  
                "label": {
                    "defaultValue": "name",
                    "type": "string",
                    "optional": False,
                    "description": "The label you want to assign to emails.",
                },
            },
        },
    )