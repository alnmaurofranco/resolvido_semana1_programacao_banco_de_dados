salario_base = float(input('Digite seu salario: '))
gratificacao = salario_base * 5 /100
imposto = salario_base * 7 /100
novo_salario = salario_base + gratificacao - imposto
print('Seu salário agora R$', novo_salario)