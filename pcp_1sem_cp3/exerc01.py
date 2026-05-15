# Matriz fornecida: cada linha é uma sala, cada coluna um horário [cite: 98]
temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

# Variáveis para identificar a sala com mais registros críticos [cite: 193]
maior_criticos = -1
sala_mais_critica = 0

# Percorrendo a matriz (linhas = salas) [cite: 75, 156]
for i in range(len(temperaturas)):
    soma_sala = 0
    cont_critico = 0
    sala_atual = temperaturas[i]  # Acessando o vetor da sala atual [cite: 64]

    # Percorrendo as temperaturas da sala (colunas) [cite: 96, 156]
    for j in range(len(sala_atual)):
        temp = sala_atual[j]
        soma_sala += temp

        # Verificando registro crítico (>= 33) [cite: 193]
        if temp >= 33:
            cont_critico += 1

    # Calculando a média da sala [cite: 13, 193]
    media = soma_sala / len(sala_atual)
    num_sala = i + 1  # Ajuste para exibição (Sala 1, 2...)

    # Exibindo os resultados da sala conforme solicitado
    print(f"Sala {num_sala}:")
    print(f"  Média das temperaturas: {media:.2f}")
    print(f"  Quantidade de registros críticos: {cont_critico}")
    print("-" * 30)

    # Lógica para identificar a sala com maior risco [cite: 193]
    if cont_critico > maior_criticos:
        maior_criticos = cont_critico
        sala_mais_critica = num_sala

# Resultado final
print(f"A sala com a maior quantidade de registros críticos é a Sala {sala_mais_critica}.")