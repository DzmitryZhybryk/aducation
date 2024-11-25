from typing import TypeAlias

Number: TypeAlias = float | int


class Calculator:

    def divide(self, x: Number, y: Number) -> float:
        if not isinstance(x, Number) or not isinstance(y, Number):
            raise TypeError("Both argument should be newmeric")

        if y == 0:
            raise ZeroDivisionError("Cannot devide by zero")

        return x / y

    def add(self, x: Number, y: Number) -> float:
        if not isinstance(x, Number) or not isinstance(y, Number):
            raise TypeError("Both argument should be newmeric")

        return x + y
