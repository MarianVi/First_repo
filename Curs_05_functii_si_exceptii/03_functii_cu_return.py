def say_hi():
    return 'Hello'


text = say_hi()
print(text)


def suma(a, b, c):
    return a + b + c


print(suma(1, 2, 3))


def show_biggest(a, b):
    if a > b:
        print(a)
    else:
        print(b)


b = show_biggest(1, 3)  # Daca nu specificam  valoare de retur pentru functie, ea va returna implicit "None"
print(b)


def nimic():
    return


print(nimic())


def end():
    return 1
    print('test')  # Aceasta bucata de cod nu se va rula deoarece functiile se opresc cand dau de cuvantul return


end()

# EXERCITIU
'''Sa se scrie o functie care primeste ca parametru o lista de numere si 
returneaza o lista care contine doar numerele pare'''


def get_all_even_numbers(numbers):
    result = []
    for elem in numbers:
        if elem % 2 == 0:
            result.append(elem)
    return result

print(get_all_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))