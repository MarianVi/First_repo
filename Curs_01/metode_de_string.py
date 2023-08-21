# METODE DE STRING
elf = "alpha 0123456789 ASD"

#lungimea string-ului
print(len(elf))

# Replace
druid = elf.replace("alpha", "beta")
print(druid)

druid2 = elf.replace("ASD", "bon")
print(druid2)

# Printare de string partiala (SLICING)
print(elf[:10]) #metoda de string slicing primele caractere
print(elf[10:]) #ultimele caractere
print(elf[4:8]) #o "zona anume" dintr-un string


# String-ul este un tip de data IMMUTABLE (nu pot sa schimb variabila respectiva)
print(elf[0])
print(elf[19])
# elf[0] = "X"              # 'str' object does not support item assignment

# Separator pentru vizualizare in consola
separator = "-" * 40
print(separator)

#numar de aparitii a unui caracter COUNT
print(elf.count("a")) #numararea caracterului "a" in string (! case sensitive)
print(elf.count("alpha"))

print(separator)

nume = "kogalniceanu"
print(nume.upper())
print(nume.capitalize())

print(separator)

print(nume.find("ala")) # "-1" inseamna ca nu gaseste
print(nume.find("cea"))

