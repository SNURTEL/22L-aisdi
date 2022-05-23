import re


def regex_find(pattern: str, text: str):
    return [m.start(0) for m in re.finditer(pattern, text)]
