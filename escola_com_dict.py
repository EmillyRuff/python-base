#!/usr/bin/env python3
""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que
frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

# Definição dos alunos por sala usando dicionário

salas = {
    "Sala 1" : ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "Sala 2" : ["João", "Antonio", "Carlos", "Maria", "Isolda"]
}


# Criando um dicionário que indica a qual sala cada aluno pertence
aluno_sala = {aluno: "Sala 1" for aluno in salas["Sala 1"]}
aluno_sala.update({aluno: "Sala 2" for aluno in salas["Sala 2"]})

# Dicionário de atividades
atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

# Exibir alunos em cada atividade, separados por sala
for nome_atividade, lista_alunos in atividades.items():
    print(f"\n------- Alunos da atividade {nome_atividade} -------\n")

    # Criando dicionário para separar os alunos por sala
    alunos_por_sala = {"Sala 1": [], "Sala 2": []}

    for aluno in lista_alunos:
        if aluno in aluno_sala:  # Verifica se o aluno está registrado em alguma sala
            alunos_por_sala[aluno_sala[aluno]].append(aluno)

    # Exibir os alunos separados por sala
    for sala, alunos in alunos_por_sala.items():
        print(f"{sala}: {alunos}")

    print("\n" + "¨" * 40)
