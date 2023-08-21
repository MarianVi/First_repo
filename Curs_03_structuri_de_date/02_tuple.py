# TUPLE
"""
- este un tip de date IMUTABLE (nu se pot sterge, adauga, modifica valori in interiorul ei)
- sunt valori ordonate si indexabile
- pot exista mai multe valori repetate
"""

# Definim un tuple - ()
tuple_numere = (1, 2, 3)
print(f'Tuple numere : {tuple_numere}')

print("-" * 40)

lista_litere = ["a", "b", "c"]
print(f'lista litere : {lista_litere}')
lista_litere.append("d")
print(f'lista litere : {lista_litere}')

# Transformam o lista intr-un tuple:
tuple_litere = tuple(lista_litere)
print(f'Tuple litere : {tuple_litere}')

print("-" * 40)

# Pot sa le numar si sa le accesez cu index, si sa verific lungime
elem1 = tuple_litere[0]
print(f'elem1 : {elem1}')
print(f'Lungime tuple : {len(tuple_litere)}')
print(f'Count lungime tupple: {tuple_litere.count("a")}')
