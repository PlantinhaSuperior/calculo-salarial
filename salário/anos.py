funcionario = input('Nome do funcioário:\n')
salarioBase = float(input('Salário:\n'))
numeroDeDependentes = int(input('Quantidade de dependentes:\n'))
anosDeCasa = int(input('Tempo de trabalho:\n'))

if numeroDeDependentes < 4:
    anosDeCasa = int(anosDeCasa/5)
elif numeroDeDependentes >= 4:
    anosDeCasa = int(anosDeCasa/6)


salarioDependente = 0
salarioDependenteFinal = 0
if numeroDeDependentes < 4:
    i = 0
    while i < anosDeCasa:
            salarioDependente = 0
            salarioDependente = ( salarioBase / 100 ) * 4
            salarioDependenteFinal += salarioDependente
            i = i+1

elif numeroDeDependentes >= 4:
    i = 0
    while i < anosDeCasa:
            salarioDependente = 0
            salarioDependente = ( salarioBase / 100 ) * 7
            salarioDependenteFinal += salarioDependente
            i = i+1


print(salarioDependenteFinal)

