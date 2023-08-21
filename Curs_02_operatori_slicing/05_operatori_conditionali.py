# OPERATORI CONDITIONALI

# Operatorii if, else
# Sunt operatori de separare a cazurilor in cod

number = 12

if number > 12:
    print(f"Da, {number} este mai mare sau egal")
else:
    print(f"Nu, {number} nu este mai mare.")


print("-" * 40)
#Introducem else if

a, b = 10, 11
if a > b:
    print(f"Da, {a} este mai mare decat {b}")
elif a == b:
    print("Numerele sunt egale")
else:                           # implicit rezulta al 3-lea caz, a < b
    print(f"Nu, {a} nu este mai mare decat {b}")