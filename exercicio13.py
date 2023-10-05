vetor = [0] * 30

for i in range(30):
    valor = int(input(f"Digite o {i + 1}º valor inteiro: "))
    vetor[i] = valor

print("Números pares no vetor:")
for valor in vetor:
    if valor % 2 == 0:
        print(valor)

menor = min(vetor)
maior = max(vetor)
print(f"Menor valor no vetor: {menor}")
print(f"Maior valor no vetor: {maior}")

media = sum(vetor) / len(vetor)

quantidade_maiores_que_media = sum(1 for valor in vetor if valor > media)
print(f"Quantidade de valores maiores que a média: {quantidade_maiores_que_media}")