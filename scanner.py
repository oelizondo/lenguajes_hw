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

AMP = 100
PIPE = 101
GT   = 102 # >
LT   = 103 # <
EQ   = 104
LTEQ = 116
AT   = 105
CAP  = 106
LOW  = 107
END  = 108
LP   = 109
RP   = 110
INT  = 111
US   = 112
DOT  = 113
TIL  = 114 # ~
COM  = 115
CTE  = 117
VAR  = 118
ERR = 200

ALPHABET_CAP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ALPHABET_MIN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#       &     |     >     <     =     @   Mayus   Minus  $     (      )  dig   _   .     ~   ,  raro  ESP
MT = [[1,    2,    ERR,   5,   6,     7,    8,     9,   END,   LP, RP,   ERR, ERR  ERR, ERR, ERR, ERR,  0   ], # edo inicial
      [AMP,  ERR,  ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR, ERR, ERR, ERR, ERR, ERR, ERR,  ERR,  1   ], # edo 1 - ampersand
      [ERR,  PIPE, ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR, ERR, ERR, ERR, ERR, ERR, ERR,  ERR,  2   ], # edo 2 - pipe
      [ERR,  ERR,  ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR, ERR, ERR, ERR, ERR, ERR, ERR,  ERR,  GT    ], # edo 3 - >
      [ERR,  ERR,  LTEQ,  ERR,  ERR,  ERR, ERR,  ERR,  ERR,  ERR, ERR, ERR, ERR, ERR, ERR, ERR,  ERR,  ERR    ], # edo 4 - <
      [ERR,  ERR,  ERR,  ERR,    3,  ERR,  ERR,   ERR,  ERR,  ERR, ERR, ERR, ERR, ERR, ERR, ERR,  ERR,  LTEQ   ], # edo 5 - =>
      [ERR,  ERR,  ERR,  ERR,  ERR,  ERR,  ERR,   ERR,  ERR,  ERR, ERR, ERR, ERR, ERR, ERR, ERR,  ERR,  0   ], #edo 6 - =
      [ERR,  ERR,  ERR,  ERR,  ERR,  ERR,  CAP,   ERR,  ERR,  ERR, ERR, ERR, ERR, ERR, ERR, ERR,  ERR,  0   ], #edo 7 - Mayúsculas
      [ERR,  ERR,  ERR,  ERR,  CTE,  CTE,   8,     8,   CTE,  CTE, CTE,  8,    8, CTE, ERR, CTE,  CTE,  CTE ], #edo 8 - M, P, F
      [ERR,  ERR,  ERR,  ERR,  VAR,  VAR,   9,     9,   VAR,  VAR, VAR,  9,    9, VAR, ERR, VAR,  VAR,  VAR ], #edo 9 - variable
      [ERR,  ERR,  ERR,  ERR,  ERR,  ERR, ERR,   ERR,    END,  ERR, ERR,  ERR, ERR, ERR, ERR, ERR,   10,  ERR ], #edo 10  - ERROR
      ]

def filtro(c):
    if c in ALPHABET_CAP:
        return 6
    elif c in ALPHABET_MIN:
        return 7
    elif 


def main():
    print 'hello'



if __name__ == '__main__':
    main()
