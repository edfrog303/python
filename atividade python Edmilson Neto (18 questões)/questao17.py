area = float(input("Informe o tamnho em metros quadrados da área a ser pintada: "))
tipo = int(input("Escolha entre Latas de 18 litros, Galões de 3,6 litros ou mesclado:[1][2][3] "))

litro = area / 6

if tipo == 1:
	#lata
	lata = ceil(litro / 18)
	preco = lata * 80
	print(f"Com uma parede de {area:.1f}m² é necessario {lata} latas, com o preço total de R${preco:.2f}")
elif tipo == 2:
	#galão
	galao = ceil(litro / 3.6)
	preco = galao * 25
	print(f"\nCom uma parede de {area:.1f}m² é necessario {galao} latas, com o preço total de R${preco:.2f}")
elif tipo == 3:
	#mesclado
	litro = (litro * 0.10) + litro
	qt_lata = 0
	qt_galao = 0
	#descobre a quantidade de latas
	while litro >= 18:
		lata = ceil(litro / 18)
		qt_lata += 1
		litro -= 18
	#descobre a quantidade de galões
	while litro > 0:
		galao = ceil(litro / 3.6)
		qt_galao += 1
		litro -= 3.6
	#preco total
	preco = (qt_lata * 80) + (qt_galao * 25)
	print(f"\nCom uma parede de {area:.1f}m² é necessario {qt_galao} galões e {qt_lata} latas, com o preço total de R${preco:.2f}")
else:
	print("escolha um tipo")
