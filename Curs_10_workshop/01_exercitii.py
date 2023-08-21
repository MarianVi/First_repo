"""
1. Singleton
Se da următoarea clasa:

class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:

a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton pentru a obține mereu același obiect:
Vom folosi functia `__new__` (adevăratul constructor din Python)
Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima apelare a lui __new__
La orice alta apelare, vom returna obiectul deja existent
"""


class PresedinteRomania:
    _instance = None

    def __new__(cls):
        """
        Metoda speciala __new__ este responsabila pentru crearea instantei obiectului.
        In majoritatea cazurilor nu avem nevoie sa suprascriem aceasta metoda, dar pentru Singleton, acesta este
            locul in care ne asiguram ca exista doar o singura instanta.
        """
        if cls._instance is None:
            cls._instance = super(PresedinteRomania, cls).__new__(cls)
            # Verificam daca exista deja o instanta, daca nu, cream una noua
            # Metoda super() ofera o cale de a apela metode din clasa de baza (parinte), in acest caz avem obiect
        return cls._instance

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'


a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')
print('-' * 40)

"""
2. Factory Pattern
Acest pattern ne permite sa creăm un obiect dintr-o clasa folosind o alta clasa (fabrica). 
Fabrica are posibilitatea de a crea obiecte din mai multe clase (de obicei aceste clase sunt siblings, 
adica mostenesc de la acelasi parinte).


Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română în limba specificata
translations va fi un dicționar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa
localize va fi o funcție care pentru un parametru de intrare, ne va da traducerea lui în acea limba 
(exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa) numita
 get_translator(language) – in functie de parametrul language, returnează un translator object.


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')
"""


class Fabrica:
    def __init__(self, translations):
        self.translations = translations

    def localize(self, word):
        return self.translations.get(word, 'Translation not available')


class EnglishTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {
                'masina': 'car',
                'barbat': 'man',
                'femeie': 'woman',
                'copil': 'child'
            }
        )


class FrenchTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {
                'masina': 'voiture',
                'barbat': 'homme',
                'femeie': 'femme',
                'copil': 'enfant'
            }
        )


class SpanishTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {
                'masina': 'coche',
                'barbat': 'hombre',
                'femeie': 'mujer',
                'copil': 'nino'
            }
        )


class TranslatorFactory():
    @classmethod
    def get_translator(cls, language):
        if language == 'en':
            return EnglishTranslator()
        elif language == 'fr':
            return FrenchTranslator()
        elif language == 'es':
            return SpanishTranslator()
        else:
            return ValueError('Invalid language code')


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
french_trans = factory.get_translator('fr')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In franceza zicem {french_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')

print('-' * 40)

from abc import ABC, abstractmethod


class TranslatorInterface(ABC):
    @staticmethod
    @abstractmethod
    def localize(word):
        pass


class EnTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'car',
        'barbat': 'man',
        'femeie': 'woman',
        'copil': 'child'
    }

    @staticmethod
    def localize(word):
        return EnTranslator.traduceri.get(word, word)  # prima - ce returneaza, a doua - ce returneaza daca NU


class FrTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'voiture',
        'barbat': 'homme',
        'femeie': 'femme',
        'copil': 'enfant'
    }

    @staticmethod
    def localize(word):
        return FrTranslator.traduceri.get(word, word)


class EsTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'coche',
        'barbat': 'hombre',
        'femeie': 'mujer',
        'copil': 'nino'
    }

    @staticmethod
    def localize(word):
        return EsTranslator.traduceri.get(word, word)


print(f'In engleza ii zicem {EnTranslator.localize("masina")}')
print(f'In franceza ii zicem {FrTranslator.localize("masina")}')
print(f'In spaniola ii zicem {EsTranslator.localize("masina")}')

print('-' * 40)

"""
3. Generators

Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
Ultima apelare va da un singur număr de “noroc” format din 7 cifre
"""
import random


def LotoGenerator():
    lista = random.sample(range(1, 50), 6)
    for i in lista:
        yield i

    yield random.randint(1_000_000, 9_000_000)


for val in LotoGenerator():
    print(val)

print('-' * 40)


def LotoGenerator2():
    l = []
    for i in range(6):
        numar = random.randint(1, 50)
        while numar in l:
            numar = random.randint(1, 50)
        l.append(numar)
        yield numar

    yield random.randint(1_000_000, 9_000_000)


for numar in LotoGenerator2():
    print(numar)

print('-' * 40)

"""         
4. Context Managers
Se da un fisier text hello.txt, care contine un text scurt. Deschideți fișierul și citiți conținutul, folosind urmatoarele 2 metode:
try - finally
Fișierul se deschide înainte de try, folosind functia open
În interiorul try citim conținutul folosind functia read
În finally se închide fișierul
with (context manager)
Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul, deoarece context managerul face asta pentru noi.
"""

f = open('Hello.txt', 'r')
try:
    print(f.read())
finally:
    f.close()

# Varianta 2

with open('Hello.txt', 'r') as f:
    print(f.read())

print('-' * 40)

"""
5. Decorators
Implementați următorii decoratori:
timeit – decorator care măsoară timpul de execuție al unei funcții
logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții
"""

import time


def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Data intrare args {args}')
        print(f'Data intrare kwargs {kwargs}')
        result = func(*args, **kwargs)
        print(f'Date iesire {result}')
        return result

    return wrapper


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(f'Functia {func.__name__} a rulat in {stop - start:.5f} secunde')
        # func.__name__ --> permite afisarea numelui functiei, ii dam acces la numele functiei
        return result

    return wrapper


def salut(func):
    def wrapper(*args, **kwargs):
        print('Salut')
        return func(*args, **kwargs)

    return wrapper  # functia se declara neapelat (fara paranteze)



@logger
def descrie_vremea(grade):
    time.sleep(2)
    return f'Vremea e frumoasa, sunt {grade} de grade!'


print(descrie_vremea(30))

