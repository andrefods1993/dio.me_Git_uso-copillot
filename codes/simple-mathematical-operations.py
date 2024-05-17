# Solicita dois números do usuário
while True:
    try:
        numero1 = float(input("Por favor, insira o primeiro número: ").strip())
        numero2 = float(input("Por favor, insira o segundo número: ").strip())
        break  # Sai do loop se as entradas forem números válidos
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Realiza operações aritméticas
adicao = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

# Verifica se o segundo número é zero antes de realizar a divisão
if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Indefinida (divisão por zero)"

# Imprime os resultados das operações
print(f"\nResultados das operações entre {numero1} e {numero2}:")
print(f"Adição: {numero1} + {numero2} = {adicao}")
print(f"Subtração: {numero1} - {numero2} = {subtracao}")
print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao}")
print(f"Divisão: {numero1} / {numero2} = {divisao}")
