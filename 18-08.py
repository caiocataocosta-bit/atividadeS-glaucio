alturas = []
generos = []

for i in range(15):
    altura = float(input("Digite a altura da pessoa " + str(i+1) + ": "))
    while altura > 2.2 or altura <= 0:
        print("Altura inválida! Digite um valor até 2.2")
        altura = float(input("Digite a altura da pessoa " + str(i+1) + ": "))

    genero = input("Digite o gênero (Masculino/Feminino): ")
    while genero != "Masculino" and genero != "Feminino" and genero != "M" and genero != "F":
        print("Gênero inválido! Digite Masculino, Feminino, M ou F")
        genero = input("Digite o gênero (Masculino/Feminino): ")

    if genero == "M":
        genero = "Masculino"
    elif genero == "F":
        genero = "Feminino"

    alturas.append(altura)
    generos.append(genero)

maior = alturas[0]
menor = alturas[0]
for a in alturas:
    if a > maior:
        maior = a
    if a < menor:
        menor = a

soma_masculino = 0
qtd_masculino = 0
qtd_feminino = 0

for i in range(15):
    if generos[i] == "Masculino":
        soma_masculino = soma_masculino + alturas[i]
        qtd_masculino = qtd_masculino + 1
    elif generos[i] == "Feminino":
        qtd_feminino = qtd_feminino + 1

if qtd_masculino > 0:
    media_masculino = soma_masculino / qtd_masculino
else:
    media_masculino = 0

print("Maior altura:", maior)
print("Menor altura:", menor)
print("Média de altura dos homens:", media_masculino)
print("Número de mulheres:", qtd_feminino)