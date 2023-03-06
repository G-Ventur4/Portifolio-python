import random

def lançamento_dado():
  return random.randint(1, 6)

acertos = 0
jogadas = 0
while True:
  num = int(input("Digite um número entre 1 e 6 (0 para sair): "))
  if num == 0 or num < 1 or num > 6:
    break
  jogadas += 1
  resultado = lançamento_dado()
  if num == resultado:
    acertos += 1
    print("Você acertou!")
  else:
    print("Você errou. O resultado foi", resultado)

print("Número de acertos:", acertos)
print("Quantidade de jogadas:", jogadas)
