# Solicita uma string do usuário
texto = input("Por favor, insira uma string: ").strip()

# Valida se a entrada é uma string não vazia
while not texto:
    texto = input("A string não pode estar vazia. Por favor, insira uma string: ").strip()

# Solicita um número inteiro do usuário
while True:
    try:
        numero = int(input("Por favor, insira um número inteiro: ").strip())
        break  # Sai do loop se a entrada for um número inteiro válido
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

# Usa um loop for para repetir a string o número de vezes informado, em linhas diferentes
for _ in range(numero):
    print(texto)

# Mensagem de saída
print("Repetição concluída.")
