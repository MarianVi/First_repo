"""
Decorators - sunt combinarea a trei concepte
"""


# Functii ca argumente

def say_hello(name):
    return f'Hello {name}'


def say_hi(name):
    return f'Hi {name}'


def greet_bob(func):
    return func('Bob')


print(greet_bob(say_hello))
print(greet_bob(say_hi))

print('-' * 40)


# Functii interne

def parent():
    def first():  # se pot defini functii in interiorul altor functii
        print('Hello from first')

    def second():
        print('Hello from second')

    second()
    first()


parent()

print('-' * 40)


# Returnare de functii

def parent(n):
    def first():
        print('First')

    def second():
        print('Second')

    if n == 1:
        return first
    return second


f = parent(1)  # f -> este o functie interna
f()

print('-' * 40)

# Decoratori simpli
import functools


def my_decorator(func):
    @functools.wraps(func)  # Se adauga pentru a nu se suprascrie functia decorata cu functia wrapper
    def wrapper():
        print('Ceva se intampla inainte de apelul functiei decorate')
        func()
        print('Ceva se intampla dupa apelul functiei decorate')

    return wrapper


@my_decorator
def say_we():
    print('Weee')


say_we()
print(say_we)
print('-' * 40)


# Decoratori pentru functii cu argumente

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@do_twice
def say_salut(name):
    print(f'Salut {name}')

say_salut('Bob')