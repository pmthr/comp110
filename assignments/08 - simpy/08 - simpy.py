# Utility class for numerical operations

from __future__ import annotations

from typing import Union

class Simpy:
    # Simpy class
    values: list[float]

    def __init__(self, values: list[float]):
        # Constructor definition
        self.values = values
    
    def __str__(self) -> str:
        # Automagic string
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        # Fill values by mutating object
        self.values = []
        i: int = 0
        while i < times:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        # Fill in a range of values
        self.values = []
        assert step != 0.0
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float:
        # Delegate this algo to the built-in sum function
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        # Operator overload for addition
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        # Operator overload for exponentation
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0 
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        # Operator overload for == 
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0 
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        # Operator overload for > 
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0 
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        # Subscription notation
        if isinstance(rhs, int):
            return self.values[rhs] 
        else:
            result: Simpy = Simpy([])
            assert len(self.values) == len(rhs)
            i: int = 0
            while i < len(self.values):
                if rhs[i] is True:
                    result.values.append(self.values[i])
                i += 1
            return result