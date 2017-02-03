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
 conectivo ::= && | || | <=> | => que representan al and, or, doble implicación y condicional
 cuantificador ::= @A | @E que representan al cuantificador universal y existencial
 constante, predicado y función ::= son nombres que inician con una letra mayúscula
 seguida por 0 o más letras (mayúsculas o minúsculas), dígitos o guiones bajos.
variable ::= son nombres que inician con una letra minúscula seguida por 0 o más letras
 (mayúsculas o minúsculas), dígitos o guiones bajos.
Los elementos léxicos deberán ser identificados y regresados como TOKENS por el analizador léxico
(scanner) del lenguaje, mientras que el cumplimiento de la gramática deberá ser verificado por el
analizador sintáctico (parser) mediante el reconocimiento de los elementos de la sintaxis.
A partir del léxico y la sintaxis establecidos se pueden reconocer las oraciones bien formadas, como los
ejemplos de abajo.```
