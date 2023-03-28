import os
from datetime import datetime
from typing import Callable, Dict, Any
import json
from util.exceptions import ErrorneousConfiguration

from util.paths import camel_case_to_snake_case, get_module_folders


def build_classifier_function_config(
    function: Callable,
    input_example: Dict[str, Any],
    data_type: str,
    issue_id: int,
    tabler_icon: str,
    min_refinery_version: str,
    state: str,
    type: str,
    gdpr_compliant: bool,
    kern_token_proxy_usable: bool,
    docker_image: str,
    available_for: list,
    part_of_group: list,
    integrator_inputs: dict,
):
    return build_config(
        module_type="classifier",
        execution_type="pythonFunction",
        function=function,
        input_example=input_example,
        data_type=data_type,
        issue_id=issue_id,
        tabler_icon=tabler_icon,
        min_refinery_version=min_refinery_version,
        state=state,
        type=type,
        gdpr_compliant=gdpr_compliant,
        kern_token_proxy_usable=kern_token_proxy_usable,
        docker_image=docker_image,
        available_for=available_for,
        part_of_group=part_of_group,
        integrator_inputs=integrator_inputs,
    )
    

def build_classifier_premium_config(
    function: Callable,
    input_example: Dict[str, Any],
    data_type: str,
    issue_id: int,
    tabler_icon: str,
    min_refinery_version: str,
    state: str,
    type: str,
    gdpr_compliant: bool,
    kern_token_proxy_usable: bool,
    docker_image: str,
    available_for: list,
    part_of_group: list,
    integrator_inputs: dict,
):
    return build_config(
        module_type="classifier",
        execution_type="premium",
        function=function,
        input_example=input_example,
        data_type=data_type,
        issue_id=issue_id,
        tabler_icon=tabler_icon,
        min_refinery_version=min_refinery_version,
        state=state,
        type=type,
        gdpr_compliant=gdpr_compliant,
        kern_token_proxy_usable=kern_token_proxy_usable,
        docker_image=docker_image,
        available_for=available_for,
        part_of_group=part_of_group,
        integrator_inputs=integrator_inputs,
    )


def build_classifier_learner_config(
    function: Callable,
    data_type: str,
    issue_id: int,
    tabler_icon: str,
    min_refinery_version: str,
    state: str,
    type: str,
    gdpr_compliant: bool,
    kern_token_proxy_usable: bool,
    docker_image: str,
    available_for: list,
    part_of_group: list,
    integrator_inputs: dict,
):
    return build_config(
        module_type="classifier",
        execution_type="activeLearner",
        function=function,
        input_example={"dummy": None},
        data_type=data_type,
        issue_id=issue_id,
        tabler_icon=tabler_icon,
        min_refinery_version=min_refinery_version,
        state=state,
        type=type,
        gdpr_compliant=gdpr_compliant,
        kern_token_proxy_usable=kern_token_proxy_usable,
        docker_image=docker_image,
        available_for=available_for,
        part_of_group=part_of_group,
        integrator_inputs=integrator_inputs,
    )


def build_extractor_function_config(
    function: Callable,
    input_example: Dict[str, Any],
    data_type: str,
    issue_id: int,
    tabler_icon: str,
    min_refinery_version: str,
    state: str,
    type: str,
    gdpr_compliant: bool,
    kern_token_proxy_usable: bool,
    docker_image: str,
    available_for: list,
    part_of_group: list,
    integrator_inputs: dict,
):
    return build_config(
        module_type="extractor",
        execution_type="pythonFunction",
        function=function,
        input_example=input_example,
        data_type=data_type,
        issue_id=issue_id,
        tabler_icon=tabler_icon,
        min_refinery_version=min_refinery_version,
        state=state,
        type=type,
        gdpr_compliant=gdpr_compliant,
        kern_token_proxy_usable=kern_token_proxy_usable,
        docker_image=docker_image,
        available_for=available_for,
        part_of_group=part_of_group,
        integrator_inputs=integrator_inputs,
    )

def build_extractor_premium_config(
    function: Callable,
    input_example: Dict[str, Any],
    data_type: str,
    issue_id: int,
    tabler_icon: str,
    min_refinery_version: str,
    state: str,
    type: str,
    gdpr_compliant: bool,
    kern_token_proxy_usable: bool,
    docker_image: str,
    available_for: list,
    part_of_group: list,
    integrator_inputs: dict,
):
    return build_config(
        module_type="extractor",
        execution_type="premium",
        function=function,
        input_example=input_example,
        data_type=data_type,
        issue_id=issue_id,
        tabler_icon=tabler_icon,
        min_refinery_version=min_refinery_version,
        state=state,
        type=type,
        gdpr_compliant=gdpr_compliant,
        kern_token_proxy_usable=kern_token_proxy_usable,
        docker_image=docker_image,
        available_for=available_for,
        part_of_group=part_of_group,
        integrator_inputs=integrator_inputs,
    )


def build_extractor_learner_config(
    function: Callable,
    data_type: str,
    issue_id: int,
    tabler_icon: str,
    min_refinery_version: str,
    state: str,
    type: str,
    gdpr_compliant: bool,
    kern_token_proxy_usable: bool,
    docker_image: str,
    available_for: list,
    part_of_group: list,
    integrator_inputs: dict,
):
    return build_config(
        module_type="extractor",
        execution_type="activeLearner",
        function=function,
        input_example={"dummy": None},
        data_type=data_type,
        issue_id=issue_id,
        tabler_icon=tabler_icon,
        min_refinery_version=min_refinery_version,
        state=state,
        type=type,
        gdpr_compliant=gdpr_compliant,
        kern_token_proxy_usable=kern_token_proxy_usable,
        docker_image=docker_image,
        available_for=available_for,
        part_of_group=part_of_group,
        integrator_inputs=integrator_inputs,
    )

def build_generator_function_config(
    function: Callable,
    input_example: Dict[str, Any],
    data_type: str,
    issue_id: int,
    tabler_icon: str,
    min_refinery_version: str,
    state: str,
    type: str,
    gdpr_compliant: bool,
    kern_token_proxy_usable: bool,
    docker_image: str,
    available_for: list,
    part_of_group: list,
    integrator_inputs: dict,
):
    return build_config(
        module_type="generator",
        execution_type="pythonFunction",
        function=function,
        input_example=input_example,
        data_type=data_type,
        issue_id=issue_id,
        tabler_icon=tabler_icon,
        min_refinery_version=min_refinery_version,
        state=state,
        type=type,
        gdpr_compliant=gdpr_compliant,
        kern_token_proxy_usable=kern_token_proxy_usable,
        docker_image=docker_image,
        available_for=available_for,
        part_of_group=part_of_group,
        integrator_inputs=integrator_inputs,
    )


def build_generator_learner_config(
    function: Callable,
    data_type: str,
    issue_id: int,
    tabler_icon: str,
    min_refinery_version: str,
    state: str,
    type: str,
    gdpr_compliant: bool,
    kern_token_proxy_usable: bool,
    docker_image: str,
    available_for: list,
    part_of_group: list,
    integrator_inputs: dict,
):
    return build_config(
        module_type="generator",
        execution_type="activeLearner",
        function=function,
        input_example={"dummy": None},
        data_type=data_type,
        issue_id=issue_id,
        tabler_icon=tabler_icon,
        min_refinery_version=min_refinery_version,
        state=state,
        type=type,
        gdpr_compliant=gdpr_compliant,
        kern_token_proxy_usable=kern_token_proxy_usable,
        docker_image=docker_image,
        available_for=available_for,
        part_of_group=part_of_group,
        integrator_inputs=integrator_inputs,
    )

def build_generator_premium_config(
    function: Callable,
    input_example: Dict[str, Any],
    data_type: str,
    issue_id: int,
    tabler_icon: str,
    min_refinery_version: str,
    state: str,
    type: str,
    gdpr_compliant: bool,
    kern_token_proxy_usable: bool,
    docker_image: str,
    available_for: list,
    part_of_group: list,
    integrator_inputs: dict,
):
    return build_config(
        module_type="generator",
        execution_type="premium",
        function=function,
        input_example=input_example,
        data_type=data_type,
        issue_id=issue_id,
        tabler_icon=tabler_icon,
        min_refinery_version=min_refinery_version,
        state=state,
        type=type,
        gdpr_compliant=gdpr_compliant,
        kern_token_proxy_usable=kern_token_proxy_usable,
        docker_image=docker_image,
        available_for=available_for,
        part_of_group=part_of_group,
        integrator_inputs=integrator_inputs,
    )

def build_config(
    module_type: str,
    execution_type: str,
    function: Callable,
    input_example: Dict[str, Any],
    data_type: str,
    issue_id: int,
    tabler_icon: str,
    min_refinery_version: str,
    state: str,
    type: str,
    gdpr_compliant: bool,
    kern_token_proxy_usable: bool,
    docker_image: str,
    available_for: list,
    part_of_group: list,
    integrator_inputs: dict,
):
    markdown_description_path = os.path.join(
        f"{module_type}s",
        f"{camel_case_to_snake_case(part_of_group[0])}",
        f"{function.__name__}",
        "README.md",
    )
    source_code_refinery_path = os.path.join(
        f"{module_type}s",
        f"{camel_case_to_snake_case(part_of_group[0])}",
        f"{function.__name__}",
        "code_snippet_refinery.md",
    )

    source_code_common_path = os.path.join(
        f"{module_type}s",
        f"{camel_case_to_snake_case(part_of_group[0])}",
        f"{function.__name__}",
        "code_snippet_common.md",
    )

    for path in [markdown_description_path, source_code_refinery_path, source_code_common_path]:
        if not os.path.exists(path):
            raise ErrorneousConfiguration(f"Missing file: {path}")

    with open(markdown_description_path, "r") as f:
        markdown_description = f.read()

    with open(source_code_refinery_path, "r") as f:
        source_code_refinery = f.read()

    with open(source_code_common_path, "r") as f:
        source_code_common = f.read()

    for mandatory_field in [
        {"module_type": module_type},
        {"execution_type": execution_type},
        {"function_name": function.__name__},
        {"function_docstring": function.__doc__},
        {"markdown_description": markdown_description},
        {"source_code_refinery": source_code_refinery},
        {"source_code_common": source_code_common},
        {"input_example": input_example},
        {"data_type": data_type},
        {"issue_id": issue_id},
        {"tabler_icon": tabler_icon},
        {"min_refinery_version": min_refinery_version},
        {"state": state},
        {"type": type},
        {"gdpr_compliant": gdpr_compliant},
        {"kern_token_proxy_usable": kern_token_proxy_usable},
        {"docker_image": docker_image},
        {"available_for": available_for},
        {"part_of_group": part_of_group},
        {"integrator_inputs": integrator_inputs},
    ]:
        if not list(mandatory_field.values())[0]:
            raise ErrorneousConfiguration(
                f"Missing mandatory field: {list(mandatory_field.keys())[0]}"
            )

    config = {
        "name": " ".join(function.__name__.split("_")).capitalize(),
        "description": function.__doc__,
        "moduleType": module_type,
        "executionType": execution_type,
        "dataType": data_type,
        "sourceCodeRefinery": source_code_refinery.replace("```python\n", "").replace("```", ""),
        "sourceCodeCommon": source_code_common.replace("```python\n", "").replace("```", ""),        
        "markdownDescription": markdown_description,
        "issueId": issue_id,
        "registeredDate": datetime.now().isoformat(),
        "endpoint": function.__name__,
        "inputExample": json.dumps(input_example, indent=4),
        "tablerIcon": tabler_icon,
        "minRefineryVersion": min_refinery_version,
        "state": state,
        "type": type,
        "gdprCompliant": gdpr_compliant,
        "kernTokenProxyUsable": kern_token_proxy_usable,
        "dockerImage": docker_image,
        "availableFor": json.dumps(available_for, indent=4),
        "partOfGroup": json.dumps(part_of_group, indent=4),
        "integratorInputs": json.dumps(integrator_inputs, indent=4),
    }

    return config, state
