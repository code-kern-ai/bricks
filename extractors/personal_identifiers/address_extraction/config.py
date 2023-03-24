from util.configs import build_extractor_function_config
from util.enums import State
from . import address_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        # strapi information
        function=address_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=62,
        tabler_icon="AddressBook",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
        type="python_function",
        gdpr_compliant=True,
        kern_token_proxy_usable=False,
        docker_image=None,
        available_for=["refinery", "common"],
        part_of_group=["personal_identifiers", "gdpr_compliant"],
        # bricks integrator information
        outputs=["address"],
        integrator_inputs={
            "name": "spelling_check",
            "refineryInputType": "text",
            "constants": {
                "inputRecordAttribute": {
                    "defaultValue": "text",
                    "optional": False,
                },  
                "label": {
                    "defaultValue": "address",
                    "type": "string",
                    "optional": False,
                    "description": "The label you want to assign to addresses.",
                },
            },
        },
    )