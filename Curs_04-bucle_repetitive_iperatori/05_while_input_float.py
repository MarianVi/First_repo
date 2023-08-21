"""
DEFINIREA EXACTA A PROBLEMEI:
1. Vrem sa verificam ca input-ul de la tastatura sa fie de tip FLOAT, moment in care sa se opreasca
2. Daca nu este de tip FLOAT, continua bucla while la nesfarsit
"""
numar = 10
while True:
    numar = input("Prompter: ")
    if numar.isnumeric() or (numar.count('.') == 1 and numar.replace('.','0').isnumeric()):
        print(f'Da, acesta este un numar : {numar}')
        inmultire = float(numar) * 5
        if inmultire % 1 == 0:
            print(f'Inmultit cu 5 = {int(inmultire)}')
        else:
            print(f'Inmultit cu 5 = {inmultire}')

        break
    else:
        print(f'Imi pare rau, {numar} nu este un numar')
        print('Mai incearca o data')