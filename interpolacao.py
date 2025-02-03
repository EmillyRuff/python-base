email_tmpl = """ Olá, %(nome)s
    Tem interesse em comprar %(produto)s?
    
    Este porduto é ótimo para resolver %(texto)s
    
    Clique sgora em %(link)s
    
    Apenas %(quantidade)d disponíveis!
    
    Preço promocional %(preco).2f
    """
clientes = ["Maria", "João", "Bruno"]

for cliente in clientes: 
    print(
        email_tmpl
        % {
            "nome": cliente,
            "produto": "caneta", 
            "texto": "Ecrever muito bem", 
            "link": "https://canetaslegais.com", 
            "quantidade": 1, 
            "preco": 50.5,

        }
    )