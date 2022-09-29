print("\tFolha de Pagamento\n")

#Entrada de dados
salario_hora = float(input("Salário/hora: R$ "))
horas_mes = int(input("Horas Trabalhadas no Mês: "))

#Cálculos
salario_bruto = salario_hora * horas_mes
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (IR + INSS + sindicato)

#Imprimindo na tela
print("")
print("__________________________")
print("Salário Bruto: R$%.2f" %salario_bruto)
print("")
print("\tDescontos\n")
print("IR: R$%.2f" %IR)
print("INSS: R$%.2f" %INSS)
print("Sindicato: R$%.2f" %sindicato)
print("")
print("Salário Líquido: R$%.2f" %salario_liquido)