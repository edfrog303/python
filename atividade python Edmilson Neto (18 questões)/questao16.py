print("\tLoja de Tintas\n")

import math
metros = float(input("Metros Quadrados: "))
litros = metros / 3

latas = math.ceil(litros / 18)
preco = latas * 80

print("Quantidade de latas: %.0f" %latas)
print("R$%.2f" %preco)