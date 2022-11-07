import os
from datetime import datetime
from typing import Callable, Dict, Any
import json
from util.exceptions import ErrorneousConfiguration

from util.paths import camel_case_to_snake_case


def build_classifier_function_config(
    function: Callable,
    input_example: Dict[str, Any],
    data_type: str,
    issue_id: int,
    state: str,
):
    return build_config(
        module_type="classifier",
        execution_type="pythonFunction",
        function=function,
        input_example=input_example,
        data_type=data_type,
        issue_id=issue_id,
        state=state,
    )


def build_extractor_function_config(
    function: Callable,
    input_example: Dict[str, Any],
    data_type: str,
    issue_id: int,
    state: str,
):
    return build_config(
        module_type="extractor",
        execution_type="pythonFunction",
        function=function,
        input_example=input_example,
        data_type=data_type,
        issue_id=issue_id,
        state=state,
    )


def build_config(
    module_type: str,
    execution_type: str,
    function: Callable,
    input_example: Dict[str, Any],
    data_type: str,
    issue_id: int,
    state: str,
):
    markdown_description_path = os.path.join(
        f"{module_type}s",
        f"{camel_case_to_snake_case(execution_type)}s",
        f"{function.__name__}",
        "README.md",
    )
    source_code_path = os.path.join(
        f"{module_type}s",
        f"{camel_case_to_snake_case(execution_type)}s",
        f"{function.__name__}",
        "code_snippet.md",
    )

    for path in [markdown_description_path, source_code_path]:
        if not os.path.exists(path):
            raise ErrorneousConfiguration(f"Missing file: {path}")

    with open(markdown_description_path, "r") as f:
        markdown_description = f.read()

    with open(source_code_path, "r") as f:
        source_code = f.read()

    for mandatory_field in [
        {"module_type": module_type},
        {"execution_type": execution_type},
        {"function_name": function.__name__},
        {"function_docstring": function.__doc__},
        {"markdown_description": markdown_description},
        {"source_code": source_code},
        {"input_example": input_example},
        {"data_type": data_type},
        {"issue_id": issue_id},
        {"state": state},
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
        "sourceCode": source_code.replace("```python\n", "").replace("```", ""),
        "markdownDescription": markdown_description,
        "issueId": issue_id,
        "registeredDate": datetime.now().isoformat(),
        "endpoint": function.__name__,
        "inputExample": json.dumps(input_example, indent=4),
    }

    return config, state
