"""
    PROGRAM
Sa se scrie un program care verifica input-ul de la tastatura
"""

"""
DEFINIREA EXACTA A PROBLEMEI:
1. Vrem sa verificam ca input-ul de la tastatura sa fie de tip INT, moment in care sa se opreasca
2. Daca nu este de tip INT, continua bucla while la nesfarsit
"""

numar = 10
while True:
    numar = input('Prompter: ')
    if numar.isnumeric():
        print(f'Da, acesta este un numar : {numar}')
        print(f'Inmultit cu 5 = {int(numar) * 5}')
        break
    else:
        print(f'Imi pare rau, {numar} nu este un numar')

print('-' * 40)

