from typing import TypeVar, Generic

T = TypeVar("T", bound=int)


class OldStack(Generic[T]):

    def __init__(self):
        self._container = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def get_all(self) -> list[T]:
        return self._container

    def pop(self) -> T:
        return self._container.pop()


class NewStack[T]:

    def __init__(self):
        self._container = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def get_all(self) -> list[T]:
        return self._container

    def pop(self) -> T:
        return self._container.pop()


def get_new_nonnull_item[Z](items: list[Z]) -> Z | None:
    for item in items:
        if item is not None:
            return item
    return None