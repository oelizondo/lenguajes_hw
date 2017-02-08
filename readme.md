## Tarea 2
### Lenguaje de Programación

### *Sintaxis*:
```
<Formula> ::= <Oracion> $
<Oracion> ::= <OracionAtomica> | <OracionCompleja>

<OracionAtomica> ::= predicado(<Terminos>)
                    | <Termino> = <Termino>

<OracionCompleja> ::= <Oracion> conectivo <Oracion>
                       | cuantificador.variable(<Oracion>)
                       | ~ <Oracion>
                       | (<Oracion>)

<Terminos> ::= <Termino> , <Terminos> | <Termino>
<Termino> ::= función(<Terminos>) | constante | variable
```

### *Léxico*:
```
 conectivo ::= && | || | <=> | => que representan al and, or, doble implicación y condicional.

 cuantificador ::= @A | @E que representan al cuantificador universal y existencial

 constante, predicado y función ::= son nombres que inician con una letra mayúscula
 seguida por 0 o más letras (mayúsculas o minúsculas), dígitos o guiones bajos.

variable ::= son nombres que inician con una letra minúscula seguida por 0 o más letras
 (mayúsculas o minúsculas), dígitos o guiones bajos.
```

### *Usar*:
```console
python

>>> from parser import parser
>>> parser()
@A.x1 (Cartero(x1) => @E.y2 (Perro(y2) && Muerde(y2, x1))) $

```