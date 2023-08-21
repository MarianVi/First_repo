class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(f'My name is: {self.name}')


class Student(Person):
    pass


p = Person(30, 'Toni')
p.print_name()
s = Student(22, 'Andi')
s.print_name()

# util in refolosirea codului

print('-' * 40)


class Angajat(Person):
    def __init__(self, age, name, loc_de_munca):
        super().__init__(age, name)
        self.loc_de_munca = loc_de_munca

    def print_work(self):
        print(f'I work at {self.loc_de_munca}')


a = Angajat(30, 'John', 'Oracle')
a.print_name()
a.print_work()
