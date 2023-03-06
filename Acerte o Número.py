import random

acertos = 0

for i in range(15):
  num = int(input("Digite um número entre 1 e 50: "))
  if num < 1 or num > 50:
    break
  resultado = random.randint(1, 50)
  if num == resultado:
    acertos += 1
    print("Você acertou! Parabéns!")
  elif num < resultado:
    print("Você errou. O número é maior.")
  else:
    print("Você errou. O número é menor.")

print("Quantidade de acertos:", acertos)
