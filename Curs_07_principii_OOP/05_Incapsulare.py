"""
Incapsularea se refera la ascunderea detaliilor de implementare ale unei clase, fata de alte clase.
Exista 3 tipuri de metode si atribute:
    - public --> accesibile peste tot
    - protected --> accesibile doar in ierarhia de mostenire (_atribut)
    - private --> accesibile doar in clasa (__atribut)
"""


class Car:
    def __init__(self, model):
        self.__model = model

    @property  # Setare ca proprietate a campului __model
    def model(self):
        print('Setare ca proprietate:')
        return self.__model

    @model.setter
    def model(self, value):
        if value.startswith('B'):  # Restrictionare asignare valori atributului __model
            print('Nu se pot adauga modele care incep cu litera B')
            return
        print('Schimbare valoare model:')
        self.__model = value

    @model.getter
    def model(self):
        print('Returnare valoare:')
        return self.__model

    @model.deleter  # Eliberarea din memorie a valorii din campul __model
    def model(self):
        print('Stergere valoare:')
        self.__model = None


c = Car('Dacia')
print(c.model)  # Se apeleaza getter-ul

c.model = 'Volvo'
print(c.model)  # Se apeleaza setter-ul

c.model = 'BMW'
print(c.model)

del c.model  # Se apeleaza deleter-ul
print(c.model)
