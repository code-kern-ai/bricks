from util.configs import build_extractor_function_config
from util.enums import State
from . import zipcode_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=zipcode_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=47,
        tabler_icon="Zip",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,  
        gdpr_compliant=True,
        kern_token_proxy_usable=False,
        docker_image=None,
        available_for=["refinery", "common"],
        part_of_group=["personal_identifiers", "gdpr_compliant"],
        # bricks integrator information
        outputs=["zip code"],
        integrator_inputs={
            "name": "zipcode_extraction",
            "refineryInputType": "text",
            "refineryOutputType": "label_position",
            "constants": {
                "inputRecordAttribute": {
                    "defaultValue": "text",
                    "optional": False,
                },  
                "countryID": {
                    "defaultValue": "DE",
                    "type": "string",
                    "optional": False,
                    "description": "The country you want to extract zipcodes from.",
                },
                "label": {
                    "defaultValue": "zip code",
                    "type": "string",
                    "optional": False,
                    "description": "The label you want to assign to emails.",
                },
            },
        },
    )