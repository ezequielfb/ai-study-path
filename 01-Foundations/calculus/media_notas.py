#Em IA, tudo é dado, e dados geralmente vem em listas, esse script é um calculo simples de notas de alunos.

# Definindo uma lista de notas
notas = [8.5, 7.0, 9.5, 6.0, 10.0]

# variavel para armazenar a soma das notas
soma = 0

# loop para somar cada 'nota' na lista 'notas'
for nota in notas:
    print(f'Somando nota: {nota}')
    soma += nota
    
# Calculando a média
quantidade = len(notas)
media = soma / quantidade

print("-" * 20)
print(f'A média das notas é: {media:.2f}')

# logica condicional simples

if media >= 7.0:
    print("Aluno aprovado, parabens!")
else:
    print("Aluno reprovado, estude mais!")