class Dog:

    def __init__(self, age, name):
        self.age = age
        self.name = name

        # Magic methods / Dunder methods

    def __str__(self):  # --> Se va apela de fiecare data cand se printeaza un obiect
        # de tipul Dog, sau se apeleaza functia str
        return f'Age: {self.age}, Name: {self.name}'

    def __repr__(self):
        return str(self)    # sau return self.__str__()
    #   return f'Age: {self.age}, Name: {self.name}' --> folosim varianta de mai sus, ca sa nu avem cod duplicat

    def __eq__(self, other):    # Comparatia se face self == other
        if not isinstance(other,Dog):   # verificam daca obiectul other apartine clasei Dog
            return False
        return self.age == other.age and self.name == other.name

d = Dog(4, 'Rex')
d2 = Dog(14, 'Bruno')
print(d)
print(d2)

print('-' * 40)
t = str(d)  # Aici se apeleaza tot functia __str__ din clasa Dog
print(t)

# -------------------------------------------------

l = [d, d2] # Lista cu obiecte de tip DOg
print(l)    # Lista contine referinta catre obiectele de tipul DOg, asa ca nu se apeleaza functia __str__ ci functia
            # __repr__

# -------------------------------------------------

d3 = Dog(1, 'Pufi')
d4 = Dog(1, 'Pufi')

print(d3 == d4)
print(d3 == 7)