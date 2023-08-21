"""
Se defineste o clasa care nu poate exista de sine statatoare
Forteaza anumite comportamente asupra claselor existente
O clasa abstraca este o clasa care are cel putin o functie abstracta (fara implementare)
"""

from abc import ABC, abstractmethod  # abc - Abstract Base Class


class Animal(ABC):  # Clasele abstracte trebuie sa mosteneasca din ABC
    @abstractmethod
    def sound(self):
        pass  # Functiile abstrace sunt functii fara implementare

    @abstractmethod
    def sleep(self):
        raise NotImplementedError


class Dog(Animal):
    def sound(self):
        print('woof')

    def sleep(self):
        print('Zzzz')


class Cat(Animal):
    def sound(self):
        print('Miau')

    def sleep(self):
        print('Prrrr')

"""a = Animal()
a.sleep()"""        # Eroare --> pentru ca nu se pot instantia clase abstracte

