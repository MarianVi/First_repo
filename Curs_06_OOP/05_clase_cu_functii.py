class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def get_name(self):
        return f'Eu sunt {self.name}'

    def bark(self):  # Self --> referinta catre obiectul curent (trebuie sa apara mereu si este mereu primul)
        print('ham ham')


d = Dog(age=5, name='Rex')
d.bark()

print(d.get_name())
