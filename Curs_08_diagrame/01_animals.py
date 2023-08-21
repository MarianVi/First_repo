from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Creature(ABC):
    @abstractmethod
    def eat(self):
        pass


class Animal(Creature):
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def eat(self):
        print(f'I am an eating: {self.__class__.__name__}')


class WildAnimal(Animal):
    def __init__(self, age, weight, location):
        super().__init__(age, weight)
        self._location = location

    @property
    def location(self):
        return self.location

    @location.setter
    def location(self, value):
        self.location = value


class DomesticAnimal(Animal):
    def __init__(self, age, weight, owner):
        super().__init__(age, weight)
        self.owner = owner


class JungleAnimal(WildAnimal):
    def __init__(self, age, weight):
        super().__init__(age, weight, 'Jungle')

    @property  # se foloseste pentru a crea proprietatea
    def location(self):
        return self._location

    @location.setter  # se foloseste pentru a restrictiona setarea valorii pt acest atribut
    def location(self, value):
        raise Exception('Nu se poate schimba aceasta valoare')


class ForestAnimal(WildAnimal):
    def __init__(self, age, weight):
        super().__init__(age, weight, 'Forest')

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        raise Exception('Nu se poate schimba aceasta valoare')


class Pet(DomesticAnimal):
    def __init__(self, age, weight, owner, name):
        super().__init__(age, weight, owner)
        self.name = name


me = Person('Vlad', 29)
cow = DomesticAnimal(10, 150, me)
dog = Pet(5, 15, me, 'Pufi')
wolf = ForestAnimal(10, 60)

# wolf.location = 'Ferma'       # Aici da eroare pentru ca am creat un setter in clasa Forest Animal
                                # care nu lasa sa se modifice acest atribut
l = [cow, dog, wolf]
for a in l:
    print(f'I am {a.age} years old')
    a.eat()             # Aici va aparea numele corespunzator fiecarei clase, deoarece avem polimorfism
