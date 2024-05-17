# Solicita um número inteiro do usuário
while True:
    try:
        numero = int(input("Por favor, insira um número inteiro: ").strip())
        break  # Sai do loop se a entrada for um número inteiro válido
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"

# Imprime o resultado
print(f"O número {numero} é {resultado}.")
