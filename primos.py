# Função para verificar se um número é primo
def is_prime(n):
    # Números menores ou iguais a 1 não são primos
    if n <= 1:
        return False
    # 2 é primo
    if n == 2:
        return True
    # Números pares maiores que 2 não são primos
    if n % 2 == 0:
        return False
    # Verifica se n é divisível por algum número ímpar até a raiz quadrada de n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    # Se não for divisível por nenhum, é primo
    return True

# Cria uma lista de números primos entre 1 e 250 (convertidos para string)
primes = [str(x) for x in range(1, 251) if is_prime(x)]

# Abre (ou cria) o arquivo results.txt para escrita
with open("results.txt", "w") as f:
    # Escreve os números primos no arquivo, um por linha
    f.write("\n".join(primes))

# Informa que o processo foi concluído com sucesso
print("Números primos entre 1 e 250 foram salvos em results.txt")
