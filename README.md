te projeto é um decorator que registra a execução de todos os scripts python


### Configurando
É necessário configurar todos os projetos com:
```
1 - um id único
2 - guardar os parâmetros de execução em uma variável
3 - especificar o motivo (reason) de estar rodando inicialmente
4 - ip da máquina que está rodando a aplicação
5 - nome da máquina ou usuário
```
### Usando o projeto

Após importar esse projeto, use em qualquer script python como mostra o exemplo abaixo

```
from decorator import *

@send_message(codigo_do_script_em_INT,"parametros passados ou nada","motivo de estar chamando","ip da maquina","nome da maquina/usuario")
def soma(a,b):
    return a+b
soma(1,2)
```
