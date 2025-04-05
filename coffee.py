from abc import ABC, abstractmethod
import json
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass
    @abstractmethod
    def description(self):
        pass
class Americano(Coffee):
    def cost(self):
        with open('cost.json', 'r') as file:
            data = json.load(file)
        return data[0]['cost']
    def description(self):
        return "Американо"
class Espresso(Coffee):
    def cost(self):
        with open('cost.json', 'r') as file:
            data = json.load(file)
        return data[1]['cost']
    def description(self):
        return "Эспрессо"
class Latte(Coffee):
    def cost(self):
        with open('cost.json', 'r') as file:
            data = json.load(file)
        return data[2]['cost']
    def description(self):
        return "Латте"
class Capuccino(Coffee):
    def cost(self):
        with open('cost.json', 'r') as file:
            data = json.load(file)
        return data[3]['cost']
    def description(self):
        return "Капучино"
class Raf(Coffee):
    def cost(self):
        with open('cost.json', 'r') as file:
            data = json.load(file)
        return data[4]['cost']
    def description(self):
        return "Лавандовый раф"
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    def cost(self):
        return self._coffee.cost()
    def description(self):
        return self._coffee.description()
class WithMilk(CoffeeDecorator):
    def cost(self):
        with open('cost.json', 'r') as file:
            data = json.load(file)
        return self._coffee.cost() + data[5]['cost']
    def description(self):
        return self._coffee.description() + ", с молоком"
class WithSyrup(CoffeeDecorator):
    def cost(self):
        with open('cost.json', 'r') as file:
            data = json.load(file)
        return self._coffee.cost() + data[6]['cost']
    def description(self):
        return self._coffee.description() + ", с сиропом"
class WithSugar(CoffeeDecorator):
    def cost(self):
        with open('cost.json', 'r') as file:
            data = json.load(file)
        return self._coffee.cost() + data[7]['cost']
    def description(self):
        return self._coffee.description() + ", с сахаром"
if __name__ == "__main__":
    americano = Americano()
    espresso = Espresso()
    print(americano.description())  # Простой кофе
    print(americano.cost())         # 100

    # Добавим молоко и сироп
    americano = WithMilk(americano)
    americano = WithSyrup(americano)

    print(americano.description())  # Простой кофе, с молоком, с сиропом
    print(americano.cost())

    print(espresso.description())  # Простой кофе
    print(espresso.cost())  # 100

    # Добавим молоко и сироп
    espresso = WithMilk(espresso)
    espresso = WithSyrup(espresso)

    print(espresso.description())  # Простой кофе, с молоком, с сиропом
    print(espresso.cost())
