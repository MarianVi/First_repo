class Dog:
    age = 12
    species = 'mammal'
    name = 'Rex'


print(Dog.age)  # --> accesare atribute direct prin referire la clasa lor
print(Dog.species)

print('-' * 40)

d = Dog()  # --> crearea unui obiect (instanta) din clasa Dog
print(d.age, d.name, d.species)

"""
In exemplul de mai sus, variabila d este o instanta a clasei Dog, iar Dog este o clasa,
deci defineste un nou tip de data.
 
Prin obiectul d, se pot accesa toate atributele clasei Dog
"""
