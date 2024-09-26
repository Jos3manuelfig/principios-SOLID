"""

El principio SOLID que se aplica aquí es el Principio de Abierto/Cerrado (Open/Closed Principle),
 que indica que las clases deben estar abiertas para extensión, pero cerradas para modificación.

Aplicación en el código:
La clase Calculator sigue este principio ya que puede extenderse para soportar nuevas operaciones sin necesidad de
modificar su código original.Esto se logra mediante el uso de la clase abstracta Operation y la
posibilidad de añadir nuevas operaciones como Addition, Substraction, etc., usando el método add_operation().
Si quisieras agregar una nueva operación (como Modulo o Exponentiation), simplemente crearías una nueva clase que
 implemente Operation y la agregarías al diccionario de operaciones, sin modificar la clase Calculator en sí.
"""

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
