#!/usr/bin/env python3
"""Bloco de Notas CLI

Uso:
    $ notes.py new "Título da Nota"
    (solicitará a tag e o texto interativamente)

    $ notes.py read tech
    (exibe todas as notas com a tag 'tech')
"""

import os
import sys
import argparse

__version__ = "0.2.0"

# Caminho para armazenar as notas
FILEPATH = os.path.join(os.curdir, "notes.txt")


def read_notes(tag: str):
    """Lê e exibe as notas que correspondem à tag fornecida."""
    if not os.path.exists(FILEPATH):
        print("Nenhuma nota encontrada.")
        return

    with open(FILEPATH, encoding="utf-8", errors="replace") as file:
        found = False
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) != 3:
                print(f"⚠ Erro: linha mal formatada -> {line.strip()}")
                continue

            title, note_tag, text = parts
            if note_tag.lower() == tag.lower():
                found = True
                print(f"📌 {title}")
                print(f"📖 {text}")
                print("-" * 30)

        if not found:
            print(f"Nenhuma nota encontrada para a tag '{tag}'.")


def new_note(title: str):
    """Cria uma nova nota e a salva no arquivo."""
    tag = input("🏷️ Tag: ").strip()
    text = input("📝 Texto:\n").strip()

    with open(FILEPATH, "a", encoding="utf-8") as file:
        file.write(f"{title}\t{tag}\t{text}\n")

    print("✅ Nota salva com sucesso!")


def main():
    """Função principal para tratar os argumentos da linha de comando."""
    parser = argparse.ArgumentParser(description="Bloco de notas simples")
    subparsers = parser.add_subparsers(dest="command")

    # Comando 'new'
    new_parser = subparsers.add_parser("new", help="Adiciona uma nova nota")
    new_parser.add_argument("title", help="Título da nota")

    # Comando 'read'
    read_parser = subparsers.add_parser("read", help="Lê notas pela tag")
    read_parser.add_argument("tag", help="Tag da nota a ser lida")

    args = parser.parse_args()

    if args.command == "new":
        new_note(args.title)
    elif args.command == "read":
        read_notes(args.tag)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()