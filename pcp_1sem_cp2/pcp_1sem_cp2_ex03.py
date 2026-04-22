cp1 = float(input("Digite a nota do Checkpoint 1: "))
cp2 = float(input("Digite a nota do Checkpoint 2: "))
cp3 = float(input("Digite a nota do Checkpoint 3: "))
sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))
gs = float(input("Digite a nota da Global Solution: "))

# Lógica para encontrar a menor nota dos checkpoints
if cp1 <= cp2 and cp1 <= cp3:
    menor_cp = cp1
elif cp2 <= cp1 and cp2 <= cp3:
    menor_cp = cp2
else:
    menor_cp = cp3

# Cálculo da média das notas (desconsiderando a menor nota do checkpoint)
# Soma das 2 maiores notas de CP + 2 Sprints, dividido por 4
soma_cp_sprints = (cp1 + cp2 + cp3 - menor_cp + sp1 + sp2)
media_simples = soma_cp_sprints / 4

# Cálculo da média final com pesos
# 40% para a média das atividades e 60% para a Global Solution
media_com_peso = (media_simples * 0.4) + (gs * 0.6)

print("-" * 30) # Escrevendo os traços no terminal
print(f"Média do semestre (sem peso): {media_simples:.1f}")
print(f"Média do semestre (com peso): {media_com_peso:.1f}")
print("-" * 30) # Escrevendo os traços no terminal