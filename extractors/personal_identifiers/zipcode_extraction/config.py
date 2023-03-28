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
        state=State.PUBLIC.value,  
        gdpr_compliant="True",
        type="python_function",
        kern_token_proxy_usable="False",
        docker_image="None",
        available_for=["refinery", "common"],
        part_of_group=["personal_identifiers", "gdpr_compliant"], # first entry should be parent directory
        # bricks integrator information
        integrator_inputs={
            "name": "zipcode_extraction",
            "refineryInputType": "text",
            "outputs":["zip code", "spanStart", "spanEnd"],
            "constants": {
                "inputAttribute": { # previously YOUR_ATTRIBUTE, never optional
                    "selectionType": "string",
                    "defaultValue": "your-text",
                }, 
                "countryID": {
                    "selectionType": "string",
                    "defaultValue": "DE",
                    "description": "The country you want to extract zipcodes from.",
                    "optional": "False",
                },
                "label": {
                    "selectionType": "string",
                    "defaultValue": "zip code",
                    "description": "The label you want to assign to zip codes.",
                    "optional": "False",
                },
            },
        },
    )