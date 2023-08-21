# OPERATORI SIMPLI

# OPERATORI DE ASIGNARE - e semnul de egal "=" - se atribuie valori
a = 5

# OPERATORI DE ADUNARE: operator aritmetic si operator de string
a, b = 'alpha', 'beta'
c = a + b
print(c)

# +, - , *, /   - operatori aritmetici (adunare, scadere, inmultire, impartire)

# RIDICARE LA PUTERE - de doua ori "**"
baza = 2
exponent = 4
x = baza**exponent
print(x)

# MODULO - "%" - echivalent cu restul impartirii: 10 (mod 3) = 1
# Ne ajuta sa vedem daca un numar este divizibil cu alt numar mai mic
numar = 10
modulo = 3
rest = numar % modulo
print(rest)

print("-" * 40)

y = 20
# intrebare: este divizibil cu 2?
print("verificam daca este divizibil cu 2: ", y % 2)
# Daca raspunsul la modulo este 0, numarul este divizibl


# IMPARTIRE INTREAGA (de cate ori intra un nr in altul)
z = 37
a = 5
print("Verificam de cate ori a intra in z: ", z // a)

print(z//a, z%a)