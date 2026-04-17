def calcular_horas_extras(salario_base, horas):
    valor_hora_extra = salario_base * 0.015
    return valor_hora_extra * horas

def calcular_descontos_faltas(salario_base, faltas):
    desconto_faltas = (salario_base * 0.02) * faltas
    return desconto_faltas

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == 's':
        if cargo == 1: return 1000.00
        elif cargo == 2: return 500.00
        elif cargo == 3: return 300.00
        elif cargo == 4: return 100.00
    return 0.0

nome = input("Digite o nome do funcionário: ")
cargo = int(input("Digite o cargo do funcionário (1 - Gerente, 2 - Analista, 3 - Assistente, 4 - Estagiário): "))
salario_base = float(input("Digite o salário base do funcionário: "))
horas = int(input("Digite o número de horas extras trabalhadas: "))
faltas = int(input("Digite o número total de faltas, no mês, do funcionário: "))
recebeu_bonus = input("O funcionário tem direito a bônus? (S/N): ").lower()


salario_bruto = salario_base
total_acrescimos = calcular_horas_extras(salario_base, horas) + calcular_bonus(cargo, recebeu_bonus)
total_descontos = calcular_descontos_faltas(salario_base, faltas)
salario_final = salario_bruto + total_acrescimos - total_descontos

print(f"\nInformações do salário de {nome}:\n")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Total de Acréscimos: R$ {total_acrescimos:.2f}")
print(f"Total de Descontos: R$ {total_descontos:.2f}")
print(f"Salário Final: R$ {salario_final:.2f}")