import os
import json
from dotenv import load_dotenv
import requests
from importlib import import_module
from typing import Dict, Any
from util.paths import camel_case_to_snake_case
from util.enums import State

load_dotenv()
CMS_BASE_URI = os.getenv("CMS_BASE_URI")
CMS_API_KEY = os.getenv("CMS_API_KEY")


def post_module(config: Dict[str, Any]):
    response = requests.post(
        f"{CMS_BASE_URI}/api/modules",
        json={
            "data": {
                "name": config["name"],
                "description": config["description"],
                "moduleType": config["moduleType"],
                "executionType": config["executionType"],
                "dataType": config["dataType"],
                "endpoint": config["endpoint"],
                "inputExample": config["inputExample"],
                "issueId": config["issueId"],
                "registeredDate": config["registeredDate"],
                "markdownDescription": config["markdownDescription"],
                "sourceCode": config.get("sourceCode"),
            }
        },
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {CMS_API_KEY}",
        },
    )
    return response


def check_module_exists(config: Dict[str, Any]):
    response = requests.get(
        f"{CMS_BASE_URI}/api/modules?filters[name][$eq]={config['name']}",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {CMS_API_KEY}",
        },
    )
    return response.json()["data"] != []


if __name__ == "__main__":
    for moduleType in ["classifier", "extractor"]:
        for executionType in ["pythonFunction"]:
            relative_dir = os.path.join(
                f"{moduleType}s", f"{camel_case_to_snake_case(executionType)}s"
            )
            for sub_dir in os.listdir(relative_dir):
                config_path = os.path.join(relative_dir, sub_dir, "config.py")
                if os.path.exists(config_path):
                    print(f"Processing {config_path}")
                    config_module = import_module(
                        f"{moduleType}s.{camel_case_to_snake_case(executionType)}s.{sub_dir}.config"
                    )
                    config, state = config_module.get_config()

                    if state == State.PUBLIC:
                        if not check_module_exists(config):
                            print("Posting module to CMS")
                            print(json.dumps(config, indent=4))
                            response = post_module(config)
                            if response.status_code == 200:
                                print("Success")
                            else:
                                print("Failed")
                                print(response.text)
                        else:
                            print(f"Module '{config['name']}' already exists")
                    else:
                        print(f"Skipping, because state is '{state}'")
                    print()
