# Regulární výrazy

_1) Předčíslí u čísla účtu_

```regex
(\d{1,6}-)?\d{6,10}/\d{4}
```

_2) Číslo účtu podruhé_

```regex
^[12][0-2]\d{4,8}/2100$
```

_3) Registrační značka_

```regex
^[0-9][ABCEHJKLMPSTUZ][0-9A-Z] [0-9]{4}$
```

_4) Telefonní číslo_

```regex
^(\+420)? ?\d{3} ?\d{3} ?\d{3}$
```

_5) Ministerstva_

```regex
Ministerstvo[\w ]*
```

_6) Slavný soude_

```regex
\d{1,2} [A-Z]{1,3} \d{1,4}/\d{4}
```

_7) Ave, Cesar!_

```regex
[IVX]+
```