# Solicita uma palavra do usuário
palavra = input("Por favor, insira uma palavra: ").strip().lower()

# Remove espaços e caracteres especiais da palavra (opcional, caso deseje ignorar espaços e pontuações)
import re
palavra_limpa = re.sub(r'[^a-zA-Z0-9]', '', palavra)

# Verifica se a palavra é um palíndromo
if palavra_limpa == palavra_limpa[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
