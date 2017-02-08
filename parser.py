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

import sys
import scanner as scanner

# Empata y obtiene el siguiente token
def match(tokenEsperado):
    global token
    if token == tokenEsperado:
        token = scanner.obten_token()
        if token == scanner.END:
            print ">>ENTRADA CORRECTA<<"
            sys.exit(1)
    else:
        error(">> ERROR LÉXICO <<")

# Funcion principal: implementa el analisis sintactico
def parser():
    global token
    token = scanner.obten_token() # inicializa con el primer token
    oracion()
    if token == scanner.END:
        print "Expresion bien construida!!"
    else:
        error(">>ERROR SINTÁCTICO<<")

# Funciones de elementos no-terminales
# modulo de elemento no terminal oracion
def oracion():
	if token == scanner.CNT:
		match(token)
		termino()
    # if token == scanner.CNT:
    #     match(token)


# modulo de elemento no terminal oracion1
def oracion1():
    if token == scanner.ROCK or token == scanner.LTEQ or token == scanner.AMP or token == scanner.PIPE:
        match(token)
        oracion()
        match(token)
        oracion1()

# modulo de elemento no terminal terminos
def terminos():
    match(token)
    termino()
    match(token)
    terminop()

# modulo de elemento no terminal termino primo
def terminop():
    match(token)
    terminos()

# modulo de elemento no terminal termino
def termino():
    if token == scanner.VAR:
        match(token)
        if token == scanner.LP:
            match(token)
            terminos()
            match(scanner.RP)

# Termina con un mensaje de error
def error(mensaje):
    print "ERROR:", mensaje
    sys.exit(1)
