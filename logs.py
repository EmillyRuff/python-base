#!/usr/bin/env python3

import logging
#nossa instancia
log = logging.Logger("logs.py")
#level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
#destino
log.addHandler(ch)


log.debug("Mensagem pro dev")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral ex: banco de dados sumiu")


print("--------")

try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    # stdout
    # stderr
