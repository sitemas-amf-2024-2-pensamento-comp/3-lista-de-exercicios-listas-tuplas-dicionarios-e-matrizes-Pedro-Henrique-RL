# Exercício 1
cores = ["vermelho", "verde", "azul", "amarelo"]
print(cores[1], cores[-1])

# Exercício 2
# a
animais = ["cachorro", "gato", "papagaio", "tartaruga"]
# b
print(animais[0], animais[-1])
# c
animais[1] = "coelho"

# Exercício 3
temperaturas = [30, 22, 25, 28, 31, 27, 29]
temperaturas = [temp + 5 if temp < 25 else temp for temp in temperaturas]
print(temperaturas)

# Exercício 4
idades = []
while True:
    idade = int(input("Digite uma idade (0 para parar): "))
    if idade == 0:
        break
    idades.append(idade)
media_idades = sum(idades) / len(idades) if idades else 0
print("Média das idades:", media_idades)

# Exercício 5
numeros = [int(input("Digite um número: ")) for _ in range(10)]
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))

# Exercício 6
sequencia1 = [int(input("Digite um número para a primeira sequência: ")) for _ in range(5)]
sequencia2 = [int(input("Digite um número para a segunda sequência: ")) for _ in range(5)]
uniao = sequencia1 + sequencia2
print("União das listas:", uniao)

# Exercício 7
lista1 = [int(input("Digite um número para a primeira lista: ")) for _ in range(5)]
lista2 = [int(input("Digite um número para a segunda lista: ")) for _ in range(5)]
comuns = [num for num in lista1 if num in lista2]
print("Elementos comuns:", comuns)

# Exercício 8
numeros = [int(input("Digite um número: ")) for _ in range(10)]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
print("Pares:", pares)
print("Ímpares:", impares)

# Exercício 9
def maior_numero(lista):
    return max(lista)

# Teste
print(maior_numero([1, 2, 3, 4, 5]))

# Exercício 10
def media(lista):
    return sum(lista) / len(lista) if lista else 0

# Teste
print(media([10, 20, 30, 40, 50]))

# Exercício 11
def contar_elementos(lista, elemento):
    return lista.count(elemento)

# Teste
print(contar_elementos([1, 2, 2, 3, 2, 4], 2))

# Exercício 12
def numeros_pares(lista):
    return [num for num in lista if num % 2 == 0]

# Teste
print(numeros_pares([1, 2, 3, 4, 5, 6]))

# Exercício 13
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# Teste
print(fibonacci(10))

# Exercício 14
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
print(meses[11])  # Substituir o índice pelo mês do seu aniversário

# Exercício 15
pontos = (100, 200, 300)
# pontos[0] = 150  # Gera um erro, pois tuplas são imutáveis

# Exercício 16
carro = {"marca": "Ford", "modelo": "Mustang", "ano": 2022}
print(carro["marca"])
print(carro["modelo"])
print(carro["ano"])

# Exercício 17
contato = {"nome": "Pedro", "telefone": "1234-5678"}
contato["telefone"] = "9876-5432"
contato["email"] = "pedro@email.com"
print(contato)

# Exercício 18
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
tabuleiro[1][1] = "X"
for linha in tabuleiro:
    print(linha)

# Exercício 19
numeros = [[2, 4], [6, 8]]
soma = sum(sum(linha) for linha in numeros)
print("Soma dos elementos:", soma)
