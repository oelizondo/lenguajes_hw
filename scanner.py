# -*- coding: utf-8 -*-
import sys
import os

# Estados Finales
AMP  = 100
PIPE = 101
GT   = 102 # >
LT   = 103 # <
EQ   = 104
LTEQ = 116 #=>
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
ROCK = 120
CNT = 121

# Arreglos
ALPHABET_CAP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ALPHABET_LOW = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
DIGITS       = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Matriz principal de estados
#       &     |     >     <     =     @   Mayus   Minus  $     (      )   dig   _    .    ~   ,   raro  ESP
MT = [[1,    2,    ERR,   5,   6,     12,    8,     9,   END,   LP,   RP,  11, ERR, 0, ERR, ERR,  ERR,  0       ], # edo inicial
      [AMP,  ERR,  ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR, ERR,  AMP    ], # edo 1 - ampersand
      [ERR,  PIPE, ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR, ERR,  PIPE   ], # edo 2 - pipe
      [ERR,  ERR,  LTEQ,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR, ERR,  GT    ], # edo 3 - >
      [ERR,  ERR,  ERR, ERR,    5,  ERR,  ERR,  ERR,   ERR,  ERR,   ERR, ERR, ERR,  ERR, ERR, ERR, ERR,  ERR    ], # edo 4 - <
      [ERR,  ERR,  ERR,  ERR,   3,  ERR,  ERR,   ERR,  ERR,  ERR,   ERR, ERR, ERR,  ERR, ERR, ERR, ERR,  LTEQ   ], # edo 5 - =>
      [EQ ,  EQ ,  ROCK, EQ ,  ERR , EQ ,  EQ ,   EQ ,  EQ ,  EQ ,   EQ , EQ , EQ , EQ , EQ , EQ , EQ ,  EQ     ], #edo 6 - =
      [ERR,  ERR,  ERR,  ERR,  ERR,  ERR,  7,   ERR,  ERR,  ERR,   ERR, ERR, ERR,   ERR, ERR, ERR, ERR,  CAP    ], #edo 7 - Mayúsculas
      [ERR,  ERR,  ERR,  ERR,  ERR,  CTE,   8,     8,   CTE,  CTE,   CTE,  8,    8, CTE, ERR, CTE, CTE,  CTE    ], #edo 8 - Mayus, Predicado, Funcion
      [ERR,  ERR,  ERR,  ERR,  VAR,  VAR,   9,     9,   VAR,  VAR,   VAR,  9,    9, VAR, ERR, VAR, VAR,  VAR    ], #edo 9 - variable
      [ERR,  ERR,  ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  END,  ERR,   ERR, ERR, ERR, ERR, ERR, ERR,  10,  ERR    ], #edo 10  - ERROR
      [INT,  INT,  INT,  INT,  INT,  INT,  INT,   INT,  END,  INT,   INT,  11, INT, INT, INT, INT,  INT, INT    ],  #edo 11 - enteros
      [CNT,  CNT,  CNT,  CNT,  CNT,  CNT,  12,   CNT,  END,  CNT,   CNT,  11, CNT, CNT, CNT, CNT,  CNT, CNT     ]]  #edo 12 - cuantificadores

def filtro(c):
    #Regresa el número de columna asociado al tipo de caracter dado(c)
    if c in ALPHABET_CAP:
        return 6
    elif c in ALPHABET_LOW:
        return 7
    elif c == '&':
        return 0
    elif c == '|':
        return 1
    elif c == '>':
        return 2
    elif c == '<':
        return 3
    elif c == '=':
        return 4
    elif c == '@':
        return 5
    elif c == '$':
        return 8
    elif c == '(':
        return 9
    elif c == ')':
        return 10
    elif c in DIGITS:
         return 11
    elif c == '_':
        return 12
    elif c == ' ' or ord(c) == 9 or ord(c) == 10 or ord(c) == 13 or ord(c) == 46 or ord(c) == 44 or ord(c) == 126: # blancos
        return 17 # 17 es raro

_c = None    # siguiente caracter
_leer = True # indica si se requiere leer un caracter de la entrada estándar
tokens = []
edo = 0
# Función principal: implementa el análisis léxico
def obten_token():
    #Implementa un analizador léxico: lee los caracteres de la entrada estándar
    global _c, _leer, tokens, edo
    edo = 0     # Estado inicial
    lexema = "" # palabra que genera el token
    while (True):
        while edo < 100:    # mientras el estado no sea ACEPTOR ni ERROR
            if _leer: _c = sys.stdin.read(1)
            else: _leer = True
            edo = MT[edo][filtro(_c)]
            if edo < 100 and edo != 0: lexema += _c
        if edo == INT:
            _leer = False
            print "(INT)"
            return INT
        elif edo == AMP:
            lexema += _c
            print "(AND)"
            return AMP
        elif edo == PIPE:
            lexema += _c
            print "(OR)"
            return PIPE
        elif edo == LTEQ:
            lexema += _c
            print "(DOBLE IMPLICACION)"
            return LTEQ
        elif edo == ROCK:
            lexema += _c
            print "(CONDICIONAL)"
            return ROCK
        elif edo == CNT:
            _leer = False
            print "(CUANTIFICADOR)"
            return CNT
        elif edo == CTE:
            _leer = False
            print "(CTE)"
            return CTE
        elif edo == VAR:
            _leer = False
            print "(VAR)"
            return VAR
        elif edo == LP:
            lexema += _c
            print "(LP)"
            return LP
        elif edo == RP:
            lexema += _c
            print "(RP)"
            return RP
        elif edo == EQ:
            lexema += _c
            print "(EQ)"
            return EQ
        elif edo == ERR:
            print "(ERR)"
            _leer = False # el último caracter no es raro
            return

        # Reinicia y lee una palabra nueva
        tokens.append(edo)
        if edo == END: return tokens
        lexema = ''
        edo = 0

def main():
    obten_token()

if __name__ == '__main__':
    main()
