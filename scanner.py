# -*- coding: utf-8 -*-
import sys
import os
# Constantes de estados Finales
# INT = 100  # Número entero
# FLT = 101  # Número de punto flotante
# OPB = 102  # Operador binario
# LRP = 103  # Delimitador: paréntesis izquierdo
# RRP = 104  # Delimitador: paréntesis derecho
# END = 105  # Fin de la entrada
# ERR = 200  # Error léxico: palabra desconocida
# COM = 108  # coma delimitador
# VAR = 109  # Variable
# Matriz de tokens
#       dig   op   (    )  raro  esp   .     $   ,    -  letras
# MT = [[  1, OPB, LRP, RRP,   4,   0,  4 , END, COM,  5 ,  5  ], # edo 0 - estado inicial
#       [  1, INT, INT, INT, INT, INT,  2 , INT, INT, INT, INT ], # edo 1 - dígitos enteros
#       [  3, ERR, ERR, ERR,   4, ERR,  4 , ERR, ERR, INT, INT ], # edo 2 - primer decimal flotante
#       [  3, FLT, FLT, FLT, FLT, FLT,  4 , FLT, FLT, INT, INT ], # edo 3 - decimales restantes flotante
#       [ERR, ERR, ERR, ERR,   4, ERR,  4 , ERR, ERR, ERR, ERR ], # edo 4 - estado de error
#       [  5, VAR, VAR, VAR, VAR, VAR, ERR, VAR, VAR,  5 ,  5  ], # edo 5 - letras, digitos, _
#       [  5, ERR, ERR, ERR, FLT, ERR, ERR, END, ERR,  5 ,  5  ]] # edo 6 - estado de error
AMP  = 100
PIPE = 101
GT   = 102 # >
LT   = 103 # <
EQ   = 104
LTEQ = 116 # <= =>   check for filter function # issue????
AT   = 105
CAP  = 106
LOW  = 107
END  = 108
LP   = 109
RP   = 110
INT  = 111
US   = 112 #_
DOT  = 113
TIL  = 114 # ~
COM  = 115
CTE  = 117
VAR  = 118
RAR  = 119
ERR  = 200

ALPHABET_CAP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ALPHABET_MIN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
DIGITS       = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#       &     |     >     <     =     @   Mayus   Minus  $     (      )   dig   _    .    ~   ,   raro  ESP
MT = [[1,    2,    ERR,   5,   6,     7,    8,     9,   END,   LP,   RP,  11, ERR, ERR, ERR, ERR,  ERR,  0    ], # edo inicial
      [AMP,  ERR,  ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR, ERR,  1    ], # edo 1 - ampersand
      [ERR,  PIPE, ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR, ERR,  2    ], # edo 2 - pipe
      [ERR,  ERR,  ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR, ERR,  GT   ], # edo 3 - >
      [ERR,  ERR,  LTEQ, ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR, ERR,  ERR  ], # edo 4 - <
      [ERR,  ERR,  ERR,  ERR,    3,  ERR,  ERR,   ERR,  ERR,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR, ERR,  LTEQ ], # edo 5 - =>
      [ERR,  ERR,  ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR, ERR,  0    ], #edo 6 - =
      [ERR,  ERR,  ERR,  ERR,  ERR,  ERR,  CAP,   ERR,  ERR,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR, ERR,  0    ], #edo 7 - Mayúsculas
      [ERR,  ERR,  ERR,  ERR,  CTE,  CTE,   8,     8,   CTE,  CTE,   CTE,  8,    8, CTE, ERR, CTE, CTE,  CTE  ], #edo 8 - M, P, F
      [ERR,  ERR,  ERR,  ERR,  VAR,  VAR,   9,     9,   VAR,  VAR,   VAR,  9,    9, VAR, ERR, VAR, VAR,  VAR  ], #edo 9 - variable
      [ERR,  ERR,  ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  END,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR,  10,  ERR  ], #edo 10  - ERROR
      [INT,  INT,  INT,  INT,  INT,  INT,  INT,   INT,  END,  INT,   INT,  11, INT, INT, INT, INT,  INT, INT  ]  #edo 11 - enteros
      ]

def filtro(c):
    #Regresa el número de columna asociado al tipo de caracter dado(c)
    if c in ALPHABET_CAP:
        return CAP - 100
    elif c in ALPHABET_MIN:
        return LOW - 100
    elif c == ',':
        return COM - 100
    elif c == '&':
        return AMP - 100
    elif c == '|':
        return PIPE - 100
    elif c == '>':
        return GT - 100
    elif c == '<':
        return LT - 100
    elif c == 'LTEQ':
        return LTEQ - 100
    elif c == '@':
        return AT - 100
    elif c == '$':
        return END - 100
    elif c == '(':
        return LP - 100
    elif c == ')':
        return RP - 100
    elif c in DIGITS:
         return 11
    elif c == '_':
        return US - 100
    elif c == '.':
        return DOT - 100
    elif c == '~':
        return TIL - 100
    elif c == ' ' or ord(c) == 9 or ord(c) == 10 or ord(c) == 13: # blancos
        return 17 # 17 es raro
    #PONER BLANKS
    else: # caracter raro
        return RAR - 100

    # Se ponen?????
    # elif c == 'CTE'
    #     return CTE - 100
    # elif c == 'VAR'
    #     return VAR - 100
    # elif c == ERR)'
    #     return ERR - 100


_c = None    # siguiente caracter
_leer = True # indica si se requiere leer un caracter de la entrada estándar
tokens = []
# Función principal: implementa el análisis léxico
def obten_token():
    #Implementa un analizador léxico: lee los caracteres de la entrada estándar
    global _c, _leer, tokens
    edo = 0 # número de estado en el autómata
    lexema = "" # palabra que genera el token
    while (True):
        while edo < 100:    # mientras el estado no sea ACEPTOR ni ERROR
            if _leer: _c = sys.stdin.read(1)
            else: _leer = True
            edo = MT[edo][filtro(_c)]
            if edo < 100 and edo != 0: lexema += _c
        if edo == INT:
            _leer = False # ya se leyó el siguiente caracter
            print "Entero", lexema
        elif edo == ERR:
            _leer = False # el último caracter no es raro
            print "ERROR! palabra ilegal", lexema

        tokens.append(edo)
        if edo == END: return tokens
        lexema = ''
        edo = 0


def main():
    obten_token()

if __name__ == '__main__':
    main()
