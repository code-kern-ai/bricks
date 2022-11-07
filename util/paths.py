from re import finditer


def camel_case_to_snake_case(text):
    matches = finditer(".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)", text)
    return "_".join([match.group(0) for match in matches]).lower()
