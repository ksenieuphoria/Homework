from typing import List, Union, Any


def add(x: int, n: int, a: str) -> Any:
    return str(x) + str(n) + a

print(add(1, 3, "7"))
print(type(add(1, 3, "7")))