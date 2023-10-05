n = int(input("n: "))
vetorX = [0] * n
vetorY = [0] * n
vetorS = [0] *n

for i in range (n):
    vetorX[i] =int(input("a:"))
    vetorY[i] =int(input("b:"))
    vetorS[i] = vetorX[i] + vetorY[i]

print(vetorX)
print('+   '*n)
print(vetorY)
print('=   '*n)
print(vetorS)