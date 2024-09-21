from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(Operation):
    def execute(self, a, b):
        return a + b


class Substraction(Operation):
    def execute(self, a, b):
        return a - b


class Multiplication(Operation):
    def execute(self, a, b):
        return a * b


class Division(Operation):
    def execute(self, a, b):
        return a / b


class Calculator:
    def __init__(self) -> None:
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f" la opereacion {name} No esta soportada .")
        return self.operations[name].execute(a, b)


calculator = Calculator()
calculator.add_operation("Addition", Addition())
calculator.add_operation("Substraction", Substraction())
calculator.add_operation("Multiplication", Multiplication())
calculator.add_operation("Division", Division())

print(calculator.calculate("Addition", 10, 12))
print(calculator.calculate("Substraction", 10, 12))
print(calculator.calculate("Multiplication", 10, 12))
print(calculator.calculate("Division", 10, 12))
