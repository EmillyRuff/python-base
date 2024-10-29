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
#__version__ + "0.0.1"  
#__autor__ + "Emilly Ruff" 
#__license__ + "Unlicense" 

# Dunder = __

current_language = "pt_BR"
# snake case (current_language)
# Pascal Case (CurrentLanguage)

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"

print(msg)