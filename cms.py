import os
import json
from dotenv import load_dotenv
import requests
from importlib import import_module
from typing import Dict, Any
from util.paths import (
    camel_case_to_snake_case,
    snake_case_to_camel_case,
    get_module_folders,
)
from util.enums import State
import fire
from wasabi import msg


load_dotenv()
CMS_BASE_URI = os.getenv("CMS_BASE_URI")
CMS_API_KEY = os.getenv("CMS_API_KEY")


class CMS:
    """Synchronizes this repository with a CMS instance.

    How to use:
    - Get a list of new modules that are not yet in the CMS: `python cms.py ls_private`
    - Publish new modules to the CMS: `python cms.py publish`
    - Update existing modules in the CMS: `python cms.py update <module_dir>`
    """

    def ls_private(self) -> None:
        """Fetches all modules from the CMS and lists all modules that are not yet in the CMS."""
        drafts = []
        ready_to_publish = []
        for moduleType in ["classifiers", "extractors", "generators"]:
            for executionType in get_module_folders(moduleType):
                relative_dir = os.path.join(
                    f"{moduleType}", f"{camel_case_to_snake_case(executionType)}"
                )
                for sub_dir in os.listdir(relative_dir):
                    config_path = os.path.join(relative_dir, sub_dir, "config.py")
                    if os.path.exists(config_path):
                        config_module = import_module(
                            f"{moduleType}.{camel_case_to_snake_case(executionType)}.{sub_dir}.config"
                        )
                        config, state = config_module.get_config()

                        module_exists, _ = check_module_exists(config)
                        if not module_exists:
                            if state == State.PUBLIC.value:
                                ready_to_publish.append(config["name"])
                            else:
                                drafts.append(config["name"])

        if len(drafts) > 0:
            print("Drafts:")
            for draft in drafts:
                print(f"\t{draft}")
        else:
            msg.info("No drafts found")
        if len(ready_to_publish) > 0:
            print("Ready to publish:")
            for module in ready_to_publish:
                print(f"\t{module}")
        else:
            msg.info("No modules ready to publish found")

    def publish(self, verbose: bool = True) -> None:
        """Publishes new modules to the CMS, if their state is PUBLIC.

        Args:
            verbose: If True, prints more information.
        """
        for moduleType in ["classifiers", "extractors", "generators"]:
            for executionType in get_module_folders(moduleType):
                relative_dir = os.path.join(
                    f"{moduleType}", f"{camel_case_to_snake_case(executionType)}"
                )
                for sub_dir in os.listdir(relative_dir):
                    config_path = os.path.join(relative_dir, sub_dir, "config.py")
                    if os.path.exists(config_path):
                        print(f"Processing {config_path}")
                        config_module = import_module(
                            f"{moduleType}.{camel_case_to_snake_case(executionType)}.{sub_dir}.config"
                        )
                        config, state = config_module.get_config()

                        if state == State.PUBLIC.value:
                            module_exists, _ = check_module_exists(config)
                            if not module_exists:
                                print("Posting module to CMS")
                                if verbose:
                                    print(json.dumps(config, indent=4))
                                response = post_module(config)
                                if response.status_code == 200:
                                    msg.good("Success")
                                else:
                                    msg.fail("Failed")
                                    print(response.text)
                            else:
                                if verbose:
                                    print(f"Module '{config['name']}' already exists")
                        else:
                            if verbose:
                                print(f"Skipping, because state is '{state}'")
                        if verbose:
                            print()

    def update(self, module_dir: str, verbose: bool = True) -> None:
        """Updates existing modules in the CMS, if their state is PUBLIC.

        Args:
            module_dir: The directory of the module to update.
            verbose: If True, prints more information.
        """

        moduleType = module_dir.split("/")[0][:-1]  # remove the trailing 's'
        executionType = snake_case_to_camel_case(module_dir.split("/")[1])
        sub_dir = module_dir.split("/")[2]
        config_path = os.path.join(module_dir, "config.py")
        if os.path.exists(config_path):
            print(f"Processing {config_path}")
            config_module = import_module(
                f"{moduleType}s.{camel_case_to_snake_case(executionType)}.{sub_dir}.config"
            )
            config, state = config_module.get_config()

            if state == State.PUBLIC.value:
                module_exists, module_data = check_module_exists(config)
                if module_exists:
                    module_data = module_data[0]
                    print("Updating module in CMS")
                    config["id"] = module_data["id"]
                    if verbose:
                        print(json.dumps(config, indent=4))
                    response = update_module(config)
                    if response.status_code == 200:
                        msg.good("Success")
                    else:
                        msg.fail("Failed")
                        print(response.text)
                else:
                    if verbose:
                        print(f"Module '{config['name']}' does not exist")
            else:
                if verbose:
                    print(f"Skipping, because state is '{state}'")
            if verbose:
                print()


def post_module(config: Dict[str, Any]):
    response = requests.post(
        f"{CMS_BASE_URI}/api/modules",
        json={
            "data": {
                "name": config["name"],
                "description": config["description"],
                "moduleType": config["moduleType"],
                "executionType": config["executionType"],
                "endpoint": config["endpoint"],
                "inputExample": config["inputExample"],
                "issueId": config["issueId"],
                "tablerIcon": config["tablerIcon"],
                "registeredDate": config["registeredDate"],
                "markdownDescription": config["markdownDescription"],
                "sourceCodeRefinery": config["sourceCodeRefinery"],
                "sourceCodeCommon": config["sourceCodeCommon"],
                "minRefineryVersion": config["minRefineryVersion"],
                "gdprCompliant": config["gdprCompliant"],
                "kernTokenProxyUsable": config["kernTokenProxyUsable"],
                "dockerImage": config["dockerImage"],
                "availableFor": config["availableFor"],
                "partOfGroup": config["partOfGroup"],
                "integratorInputs": config["integratorInputs"],
            }
        },
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {CMS_API_KEY}",
        },
    )
    return response


def update_module(config: Dict[str, Any]):
    response = requests.put(
        f"{CMS_BASE_URI}/api/modules/{config['id']}",
        json={
            "data": {
                "name": config["name"],
                "description": config["description"],
                "moduleType": config["moduleType"],
                "executionType": config["executionType"],
                "endpoint": config["endpoint"],
                "inputExample": config["inputExample"],
                "issueId": config["issueId"],
                "tablerIcon": config["tablerIcon"],
                "registeredDate": config["registeredDate"],
                "markdownDescription": config["markdownDescription"],
                "sourceCodeRefinery": config["sourceCodeRefinery"],
                "sourceCodeCommon": config["sourceCodeCommon"],
                "minRefineryVersion": config["minRefineryVersion"],  #
                "gdprCompliant": config["gdprCompliant"],
                "kernTokenProxyUsable": config["kernTokenProxyUsable"],
                "dockerImage": config["dockerImage"],
                "availableFor": config["availableFor"],
                "partOfGroup": config["partOfGroup"],
                "integratorInputs": config["integratorInputs"],
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
    if response.status_code == 200:
        return response.json()["data"] != [], response.json()["data"]
    else:
        raise Exception(response.text)


if __name__ == "__main__":
    fire.Fire(CMS)
