"""
6. Decorators extra
Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nasterii
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat, folosind un decorator `@require_login`
– o metoda logout, fara params, care delogheaza userul.


Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.
"""


def require_login(method):
    def wrapper(self, *args, **kwargs):
        if not self.loggedin:
            print('Acces nepermis, utilizatorul nu este logat')
            return
        return method(self, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, nume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.parola = parola
        self.data_nasterii = data_nasterii
        self.loggedin = False

    def login(self, email, parola):
        if self.email == email and self.parola == parola:
            self.loggedin = True
            print('Utilizatorul s-a logat cu succes')
        else:
            print('Email sau parola incorecte')

    @require_login
    def get_info(self):
        return {
            'nume': self.nume,
            'email': self.email,
            'data nasterii': self.data_nasterii
        }

    def logout(self):
        if self.loggedin:
            self.loggedin = False  # resetam ' starea ' de autentificare
            print('Utilizatorul a fost delogat')
        else:
            print('Utilizatorul nu era logat')

user = User('Ion', 'ion@itfactory.ro', 'parola', '03.06.20')
print(user.get_info())
user.login('ion@itfactory.ro', 'parola')
print(user.get_info())
user.logout()
print(user.get_info())
user.login('ion@itfactory.ro', 'parola')
print(user.get_info())