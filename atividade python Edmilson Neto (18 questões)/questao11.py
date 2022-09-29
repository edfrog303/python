print ('Programa para ver numeros')
numero1 = int(input('\nDigite o numero 1: '))
numero2 = int(input('\nDigite o numero 2: '))
numero3 = float(input('\nDigite o numero 3: '))
print ('\n a)O produto do dobro do primeiro com a metade do segundo:\n')
print ("Resposta:", int(numero1 * 2 * numero2/2))
print ('\n b)A soma do triplo do primeiro com o terceiro:\n')
if type (numero3).__name__ == 'int' :
    print("Resposta:", int(numero1 * 3 + numero3))
else:
    print ("Resposta:", numero1 * 3 + numero3)
print ('\n c)O terceiro elevado ao cubo:\n')
if type (numero3).__name__ == 'int' :
    print("Resposta:", int(numero3 ** 3))
else:
    print ("Resposta:", numero3 ** 3)