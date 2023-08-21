"""
l = [1, 2, 3]
x = iter(l) --> se obtine iteratorul specific listei 'l'
next(x) --> se parcurge element cu element - 1
next(x) - 2
next(x) - 3
next(x) --> produce eroarea StopIteration pentru ca s-au parcurs toate elementele
"""
"""
Iterator = obiect care poate fi iterat
    Orice clasa care este iterabila (adica este un iterator) trebuie sa implementeze doua metode:
            --> __iter__(self):
                    -> Aici se initializeaza iteratorul, si se returneaza clasa curenta
            --> __next__(self):
                    -> Aici se va returna mereu, urmatoarea valoare din colectia iterabila
                    -> Contine mecanismul de obtinere a valorii urmatoare in colectie
                    -> Atunci cand nu mai sunt valori disponibile, se arunca exceptia StopIteration
"""


class EvenIterator:
    def __init__(self, n):
        self.n = n  # n = cate numere pare vrem sa generam

    def __iter__(self):
        self.generated_numbers = 0  # cate numere pare am generat pana acum
        self.curent = 0  # numarul curent
        return self

    def __next__(self):
        self.curent += 1
        if self.generated_numbers >= self.n:  # Daca am generat mai multe numere decat s-a cerut, ne oprim
            raise StopIteration
        if self.curent % 2 == 0:  # urmatorul numar gasit
            self.generated_numbers += 1  # crestem contorul numerelor gasite pana acum
            return self.curent  # returnam numarul gasit
        return self.__next__()  # aici nu s-a gasit numar si se apeleaza mecanismul inca o data


it = EvenIterator(10)
for i in it:
    print(i)

print('-' * 40)

it = EvenIterator(10)
i = iter(it)
x = next(it)

while x:
    print(x)
    try:
        x = next(i)
    except StopIteration:
        x = None
