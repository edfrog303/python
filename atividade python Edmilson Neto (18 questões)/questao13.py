sexo = str(input("Digite o seu sexo 'M' para masculino e 'F' para feminino: "))
if sexo == "M":
    alturam = float(input("Digite a sua altura: "))
    MDCm = (72.7*alturam) - 58
    print(f"O seu peso ideal é {MDCm}")
    
    
else:
    if sexo == "F":
        alturaf = float(input("Digite a sua altura: "))
        MDCf = (62.1*alturaf) - 44.7
        print(f"O seu peso ideal é {MDCf}")
