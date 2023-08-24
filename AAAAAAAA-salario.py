# +3% salario base para cade dependente que ele tem (max 5)
# if dependentes < 4, funcionario +4% salarioBase / 5anos (max 6)
#if dependentes >= 4, funcionario +7% salarioBase / 6anos (max7)
#if ano bissexto +1%
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

funcionario = input('Nome do funcioário:\n')
salarioBase = float(input('Salário:\n'))


numeroDeDependentes = int(input('Quantidade de dependentes:\n')) #listagem
while numeroDeDependentes > 5:
    print('Máximo de 5 dependentes.')
    numeroDeDependentes = int(input('Quantidade de dependentes:\n'))

    
anosDeCasa = int(input('Tempo de trabalho:\n'))
ano = int(input('Ano atual:\n'))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

salarioBonus = salarioBase + ( ( salarioBase / 100 ) * ( 3 * numeroDeDependentes ) ) #cálculo de bônus salarial p/dependente

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if numeroDeDependentes < 4:
    anosDeCasa = int(anosDeCasa/5)  
elif numeroDeDependentes >= 4:      #Checa o número de dependetes e divide pela quantidade específica.
    anosDeCasa = int(anosDeCasa/6)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

salarioDependente = 0
salarioDependenteFinal = 0
if numeroDeDependentes < 4:
    i = 0
    while i < anosDeCasa:                                  #checa o número de depentes e calcula o bônus de sálarial - caso seja < 4
            salarioDependente = 0
            salarioDependente = ( salarioBase / 100 ) * 4
            salarioDependenteFinal += salarioDependente
            i = i+1

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


elif numeroDeDependentes >= 4:
    i = 0
    while i < anosDeCasa:                                  #checa o número de depentes e calcula o bônus de sálarial - caso seja >= 4
            salarioDependente = 0
            salarioDependente = ( salarioBase / 100 ) * 7
            salarioDependenteFinal += salarioDependente
            i = i+1

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
salarioAnoBissexto = 0
if ano % 4 ==0 and ano%100 !=0 or ano % 400 == 0:
    salarioAnoBissexto = ( salarioBase / 100 ) * 1
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print(f'O bônus salarial por tempo/dependente é de {salarioBonus}R$')

print(f'O bônus sálarial por dependente é de {salarioDependenteFinal}R$') 
                                                                            #Print final
print(f'O O bônus sálarial por ano bissexto é de {salarioAnoBissexto}R$')

salariofinal = salarioBase + salarioBonus + salarioDependenteFinal + salarioAnoBissexto  #cálculo do salário final

print(f'O salário final é de: {salariofinal}R$')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------