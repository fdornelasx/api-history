import sys
sys.path.append("env/src/apihistory/empiricus_utils/")

from apirequest import *

@send_message(11234,"parametros passados ou nada","running","porque alguem quis colocar isso","ip da maquina","nome da maquina/usuario")
def soma(a,b):

    return a+b

soma(1,10)
