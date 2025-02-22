#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa
exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:
    
    export LANG=pt_BR

Ou informe atraveés do CLI argument `--lang`

Ou o usuário terá que digitar.
Execução: 
    
    python3 hello.py
    ou
    ./hello.py
"""
#meta dados:
from csv import __version__


__version__ = "0.1.3" 
__autor__ = "Emilly Ruff"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    # TODO: tratar ValueError
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Logging
        print(f"[ERROR] {str(e)}")
        print("You need to use `=`")
        print(f"You passed {arg}")
        print("Try with --key=value")
        sys.exit(1)


    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option {key}")
        sys.exit()

        arguments[key] = value


# Dunder = __
current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language? ")

current_language = current_language[:5]
# snake case (current_language)
# Pascal Case (CurrentLanguage)

msg = {
    "en_US" : "Hello, World!",
    "pt_BR": "Olá, Mundo!", 
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

# sets (Hash Table) - O(1) - constante
# dicts (Hash Table)

# Ordem de Complexidade O(n)

#LBYL
if current_language in msg:
    message = msg[current_language]
else: 
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(message * int(arguments["count"]))
