"""
Singleton --> design pattern care ne permite sa avem o clasa care returneaza mereu aceeasi instanta unica
          --> de obicei se foloseste in situatii in care nu ne intereseaza obiectul in sine, ci doar anumite
                functionalitati ale acestuia

Avantaje: --> poti fi sigur ca o clasa Singleton are doar o singura instanta
          --> poti avea acces global catre aceasta instanta
          --> obiectul Singleton este initializat doar o singura data (prima data cand este cerut)

Dezavantaje: --> poate masca un design defectuos, de exemplu atunci cand componentele unui sistem stiu prea multe
                    unele despre celelalte
"""


class SingletonLogger:
    _instance = None
    # Functia __init__ in Python nu este un constructor traditional, ci doar un initializator.
    # Inainte de __init__ este apelata functia __new__ unde se creeaza defapt obiectul
    def __new__(cls, *args, **kwargs):
        # Functia __new__ nu are "self" ca prim argument pentru ca "self" nu exista inca la momentul rularii
        # In schimb avem cls, care este o referinta catre clasa curenta
        if cls._instance is None:  # Prima data cand este apelata SingletonLogger se creeaza obiectul
            print('Creating_object')
            cls._instance = super().__new__(cls)
        return cls._instance  # Returnam acelasi obiect de fiecare data


# logger = SingletonLogger()
# logger2 = SingletonLogger()
# print(logger, logger2)
# print(logger is logger2)

print('-' * 40)

class SingletonFileLogger(SingletonLogger): # Mostenirea facuta in acest fel, duce la problema
    # ca obiectul instantei Singleton poate fi de tipul SingletonLogger, nu SingletonFileLogger
    # daca el se creaza inainte
    # Ca si solutie, vezi exemplul de mai jos, cu SingletonLoggerMultiClass
    def __init__(self, file_name):
        self.file_name = file_name


sfl = SingletonFileLogger('Hello.txt')
sfl2 = SingletonFileLogger('Hello2.txt')
print(sfl, sfl2)
print(sfl.file_name, sfl2.file_name)

print('-' * 40)

class SingletonLoggerMultiClass:
    _instance = {}
    def __new__(cls, *args, **kwargs):
        if cls._instance.get(cls) is None:
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]
class SingletonFileLogger2(SingletonLoggerMultiClass):
    def __init__(self, file_name):
        self.file_name = file_name

l = SingletonLoggerMultiClass()
s = SingletonFileLogger2('Hello.txt')
l2 = SingletonLoggerMultiClass()
s2 = SingletonFileLogger2('Hello.txt')
print(l, l2)
print(s, s2)