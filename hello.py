#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa
exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:
    
    export LANG=pt_BR

Execução: 
    
    python3 hello.py
    ou
    ./hello.py
"""
#meta dados:
from csv import __version__


__version__ = "0.0.1" 
__autor__ = "Emilly Ruff"
__license__ = "Unlicense"

import os

# Dunder = __

current_language = os.getenv("LANG", "en_US")[:5]
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

print(msg[current_language])
