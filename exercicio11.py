numeros = [0] * 30
for z in range(30):
    numeros[z] = int(input('Digite um número: '))

quantidade = 0
numero = int(input('Digite o número a ser pesquisado: '))
for y in range(30):
    if numero == numeros[y]:
        quantidade += 1

print(f'O número {numero} aparece {quantidade} vezes na lista')