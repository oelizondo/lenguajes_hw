# -*- coding: utf-8 -*-

# BORRAR
# Implementacion de un parser
# Reconoce expresiones mediante la gramatica:

# EXP -> EXP op EXP | EXP -> (EXP) | cte
# la cual fue modificada para eliminar ambiguedad a:
# EXP  -> cte EXP1
# EXP1 -> (EXP) EXP1 | op EXP EXP1 | vacio

# los elementos lexicos (delimitadores, constantes y operadores)
# son reconocidos por el scanner
#

import sys
import obten_token as scanner

# Empata y obtiene el siguiente token
def match(tokenEsperado):
    global token
    if token == tokenEsperado:
        token = scanner.obten_token()
    else:
        error("token equivocado")

# Funcion principal: implementa el analisis sintactico
def parser():
    global token
    token = scanner.obten_token() # inicializa con el primer token
    exp()
    if token == scanner.END:
        print "Expresion bien construida!!"
    else:
        error("expresion mal terminada")

# Modulo que reconoce expresiones
def exp():
    if token == scanner.INT or token == scanner.FLT:
        match(token) # reconoce Constantes
        exp1()
    elif token == scanner.VAR :
        match(token)
        exp1()
    elif token == scanner.LRP:
        match(token) # reconoce Delimitador (
        exp()
        match(scanner.RRP)
        exp1()
    else:
        error("expresion mal iniciada")

# Modulo auxiliar para reconocimiento de expresiones
def exp1():
    if token == scanner.OPB or token == scanner.COM:
        match(token) # reconoce operador
        exp()
        exp1()
    elif token == scanner.LRP:
        exp()

# Termina con un mensaje de error
def error(mensaje):
    print "ERROR:", mensaje
    sys.exit(1)
