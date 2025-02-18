#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notas.py read tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    # leitura das notas
    with open(filepath, encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) != 3:
                print(f"Erro: linha mal formatada -> {line.strip()}")
                continue  # Ignora linhas com formato incorreto

            title, tag, text = parts
            if tag.lower() == arguments[1].lower():
                print(f"title: {title}")
                print(f"text: {text}")
                print("-" * 30)
                print()

elif arguments[0] == "new":
    title = arguments[1]  # TODO: tratar exceções para garantir entrada válida
    tag = input("tag: ").strip()
    text = input("text:\n").strip()

    # Salva corretamente em uma única linha com tabulações
    with open(filepath, "a", encoding="utf-8") as file_:
        file_.write(f"{title}\t{tag}\t{text}\n")

    print("Nota salva com sucesso!")