class Car:
    def go(self):
        print('vrum vrum')

    def start(self):
        print('Starting car')


class Flyable:
    def fly(self):
        print('Flu, Flu')

    def start(self):
        print('Starting flyable')

class FlyingCar(Car, Flyable):
    pass

"""
Method Resolution Order (MRO) --> regula dupa care se decide care este functia ce se
apeleaza, atunci cand se avem o mostenire multipla, functii cu acelasi nume
de la stanga la dreapta
"""

fc = FlyingCar()
fc.fly()
fc.go()
fc.start()

class FlyingCar2(Flyable, Car):
    pass

fc2 = FlyingCar2()
fc2.start()