salarioBase = int(input('Salário:\n'))
numeroDeDependentes = int(input('Quantidade de dependentes:\n'))

salarioBonus = salarioBase + ( ( salarioBase / 100 ) * ( 3 * numeroDeDependentes ) ) 

print(f'o salario bônus é de {salarioBonus}')
