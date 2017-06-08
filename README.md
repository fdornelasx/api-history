te projeto é um decorator que registra a execução de todos os scripts python


### Configurando
É necessário configurar todos os projetos com:
```
1 - um id único (tabela script)
2 - guardar os parâmetros de execução em uma variável (ou passar o sys.argv)
3 - especificar o motivo (reason) de estar rodando inicialmente (será alterado para o stacktrace, ou return final do código)
4 - ip da máquina que está rodando a aplicação
5 - nome da máquina ou usuário
```
### Usando o projeto


Lembre-se de exportar a variável de ambiente onde a API está rodando

```
export API_ENDPOINT = http://API_ENDPOINT_aqui:porta
```


No seu arquivo requirements.txt do python, você deverá colocar assim:

```
-e git+https://github.com/fillipedornelas/api-history.git#egg=apihistory
```

Após importar esse projeto, use em qualquer script python como mostra o exemplo abaixo

```
from registry_utils import apirequest

@apirequest.send_message("script_code",str(sys.argv),"running","comentarios","ip da maquina","nome da maquina/usuario")
def soma(a,b):
    return a+b
soma(1,2)
```
