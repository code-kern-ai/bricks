from re import finditer
import os

def camel_case_to_snake_case(text):
    matches = finditer(".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)", text)
    return "_".join([match.group(0) for match in matches]).lower()


def snake_case_to_camel_case(text):
    text_cased = "".join([word.capitalize() for word in text.split("_")])
    return text_cased[0].lower() + text_cased[1:]

def get_module_folders(base_folder):
    folders = os.listdir(base_folder)
    ignore_these = ["__pycache__", "README.md", "util", "zero_shot", "__init__.py", ".DS_Store", "_template"]
    for item in ignore_these:
        try:
            folders.remove(item)
        except:
            pass
    return folders

