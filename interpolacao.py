#!user/bin/env python
"""Imprime a mensagem de um e-mail"""
__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt


for line in open(filepath):
    name, email = line.split(",")

    # TODO: Susbtituir por envio de email
    print(f"Enviando email para {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "name": name,
            "produto": "caneta", 
            "texto": "Ecrever muito bem", 
            "link": "https://canetaslegais.com", 
            "quantidade": 1, 
            "preco": 50.5,
        }
    )
    print("-"*50)