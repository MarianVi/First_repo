"""
Generator = un obiect care poate crea valori care pot fi parcurse secvential, asemanator unui iterator, dar
    sunt implementati sub forme de functii
Generators = sunt acele functii care nu folosesc 'return' pentru a se opri dand inapoi o valoare, ci folosesc
    cuvantul 'yield' pentru  aceda o valoare, dupa care v-a putea reveni in aceeasi functie sa continue executia
"""


def gen():
    print('Am intrat in functia generator')
    yield 10  # yield = a ceda

    print('Am intrat din nou in functia generator')
    yield 100

    print('Am intrat a 3a oara in functia generator')
    # Aici se arunca eroarea 'StopIteration' pentru ca nu mai gaseste 'yield'


g = gen()
print(next(g))
print(next(g))

print('-' * 40)


def even_gen(n):
    generated_numbers = 0
    curent = 0
    while generated_numbers < n:
        curent += 1
        if curent % 2 == 0:
            yield curent
            generated_numbers += 1


g2 = even_gen(10)
for i in g2:
    print(i)
