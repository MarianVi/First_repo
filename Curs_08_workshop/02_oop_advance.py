"""
OOP - advance

Exerciții - studiu în workshopul de weekend

ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’

Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui

3. Actualizează proiectul pe github facand un push la noul cod
În Folderul de teme ajunge să pui doar linkul cu proiectul tău public
"""

from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descriere(cls):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura * self.__latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print('Deleter: am sters latura')
        self.__latura = None


patrat1 = Patrat(20)
patrat1.descriere()
patrat1.latura
patrat1.aria()
print(f'Latura este {patrat1.latura} si aria este {patrat1.aria()}')
patrat1.latura = 30
del patrat1.latura


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        aria_cercului =  self.PI * (self.__raza * 2)
        return aria_cercului
    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: noua latura este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print('Deleter: am sters raza')
        self.__raza = None
    def descriere(self):
        print('Eu nu am colturi')

cerc1 = Cerc(10)
cerc1.descriere()
cerc1.raza
cerc1.aria()
print(f'Raza cercului este: {cerc1.raza}')
print(f'Aria cercului este: {cerc1.aria()}')
cerc1.raza = 20
print(f'Aria cercului este: {cerc1.aria()}')
del cerc1.raza