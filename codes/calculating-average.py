# Solicita três notas do usuário
notas = []
for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Por favor, insira a nota {i}: ").strip())
            if 0 <= nota <= 10:
                notas.append(nota)
                break  # Sai do loop se a entrada for uma nota válida
            else:
                print("Por favor, insira uma nota entre 0 e 10.")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

# Calcula a média das notas
media = sum(notas) / len(notas)

# Imprime o resultado
print(f"A média das notas {notas[0]}, {notas[1]} e {notas[2]} é {media:.2f}.")
