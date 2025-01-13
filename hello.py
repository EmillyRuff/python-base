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

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjou, Monde!"


print(msg)
