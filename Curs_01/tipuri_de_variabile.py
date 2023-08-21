# TIPURI DE VARIABLIE

# Variabila de tip "INT" (numar intreg)
a = 12
b = -16

# Variabila de tip "FLOAT" (numar zecimal)
pi = 3.14159

# Variabila de tip "STRING" (sir de caractere)
# Intotdeauna se pune intre ghilimele duble sau simple
d = "Ana are mere 123!@#$%@#$%@#$%^ASDAGJH#$%^"
e = 'Ana are mere'
# e = Ana are mere          # nu e corect definit pentru ca nu are ""


# Variabila de tip "BOOLEAN" (valori adevarat / fals)
f = True
g = False


# Acesta este un comentariu pe o singura linie
# Acesta este alt comentariu pe o singura linie

"""Acesta este un comentariu 
Pe mai multe linii
Folosim ghilimele multiple
Simple sau duble"""

'''Hai sa facem
cu ghilimele simple'''


# Numele variabilelor sunt mereu cu litere mici si cu "_" daca e nume compus
# ASIGNARE MULTIPLA DE VARIABILA
mama, tata = "Oana", "George"
varsta_mama = 40

# TIPURI DE PRINT
print(mama) # la printare de variabila nu se folosesc ghilimele
print("Pe mama o cheama:", mama, "si pe tata:", tata)
print("Pe mama o cheama:" + mama + "; pe tata il cheama:" + tata) # "+" elimina spatiul, fata de "," care adauga spatiu
print("Pe mama o cheama:" + mama + " " + str(varsta_mama))
print(f"Pe mama o cheama {mama} si are {varsta_mama} ani")  # f-string - folosesti o variabila intr-un string
print(f"Pe mama o cheama {mama} si are {varsta_mama} ani")  # f-string - folosesti o variabila intr-un string