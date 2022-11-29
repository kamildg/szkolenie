from typing import Any


def get_ci(d: dict[str, Any], key: str) -> Any:
    for k, v in d.items():
        if key.lower() == k.lower():
            return v


def concatenate(first: str, second: str, /, *, delim: str):
    return delim.join([first, second])


def concatenate2(*items, delim: str):
    return delim.join(items)


print(concatenate("jan", "kowalski", delim=" "))
print(concatenate2("jan", "kowalski", delim=" "))