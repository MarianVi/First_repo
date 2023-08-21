# OPERATORI LOGICI

# "and" - echivalent cu "si"
# "and" este un operator care verifica valoare de adevar a mai multor elemente
# si acesta si celalalt trebuie sa aiba valoare de adevar (ambele)
acesta, celalalt = True, True
print("acesta and celalalt: ",acesta and celalalt) # True and True
acesta, celalalt = True, False
print("acesta and celalalt: ",acesta and celalalt) # True and False
acesta, celalalt = False, True
print("acesta and celalalt: ",acesta and celalalt) # False and True
acesta, celalalt = False, False
print("acesta and celalalt: ",acesta and celalalt) # False and False


print("-" * 40)

# Operatorul "or" (Sau)
# fie alpha, fie beta trebuie sa aiba valoare de adevar (oricare din ele)
alpha, beta = True, True
print("alpha or beta: ", alpha or beta) # True or True
alpha, beta = True, False
print("alpha or beta: ", alpha or beta) # True or False
alpha, beta = False, True
print("alpha or beta: ", alpha or beta) # False or True
alpha, beta = False, False
print("alpha or beta: ", alpha or beta) # False or Flase
