"""
Principio SOLID de Sustitución de Liskov (Liskov 
Substitution Principle, LSP)
El principio de sustitución de Liskov (Liskov Substitution Principle, LSP) es el tercer principio de SOLID y establece que:

"Los objetos de una clase derivada deben poder reemplazar a los objetos de su clase base sin alterar el correcto funcionamiento del programa."

En otras palabras, una subclase debe poder ser utilizada en lugar de su clase base sin que el programa tenga comportamientos inesperados o erróneos. Para cumplir con este principio, las subclases no deben alterar el comportamiento esencial de los métodos heredados de la clase base.


""" """
Ejercicio
"""

# Incorrecto


class Bird:
    def fly(self):
        return "Flying"


class Chicken(Bird):
    def fly(self):
        raise Exception("Los pollos no vuelan")


# bird = Bird()
# bird.fly()
# chicken = Chicken()
# chicken.fly()

# Correcto


class Bird:
    def move(self):
        return "Moving"


class Chicken(Bird):
    def move(self):
        return "Walking"


bird = Bird()
print(bird.move())
chicken = Chicken()
print(chicken.move())

bird = Chicken()
print(bird.move())
chicken = Bird()
print(chicken.move())

"""
Extra
"""


class Vehicle:

    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"Velocidad: {self.speed} Km/h")

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} Km/h")


class Car(Vehicle):
    def accelerate(self, increment):
        print("El coche está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("El coche está frenando")
        super().brake(decrement)


class Bicycle(Vehicle):
    def accelerate(self, increment):
        print("La bicicleta está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La bicicleta está frenando")
        super().brake(decrement)


class Motorcycle(Vehicle):
    def accelerate(self, increment):
        print("La moto está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La moto está frenando")
        super().brake(decrement)


def test_vehicle(vehicle):
    vehicle.accelerate(2)
    vehicle.brake(1)


car = Car()
bicycle = Bicycle()
motorcycle = Motorcycle()

test_vehicle(car)
test_vehicle(bicycle)
test_vehicle(motorcycle)
