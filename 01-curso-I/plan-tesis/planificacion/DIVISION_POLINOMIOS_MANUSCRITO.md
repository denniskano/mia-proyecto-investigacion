# División de polinomios — guía para redactar a mano (máx. 1 cara)

> Copiar con lápiz en una hoja en blanco. Usa la **versión compacta** si necesitas que quepa en una sola cara.

---

## VERSIÓN COMPACTA PARA COPIAR (1 cara)

**Dirigido a:** estudiantes que ya suman, restan y multiplican polinomios.  
**Idea a transmitir:** la división es un procedimiento repetitivo; siempre hay cociente y residuo, y el grado del residuo es menor que el del divisor.  
**Conocimientos previos:** término líder, potencias descendentes, coeficiente 0 en términos ausentes.

**Inicio.** Dividir polinomios significa hallar el cociente Q(x) y el residuo R(x) que cumplen la igualdad fundamental:

```
        D(x)  =  Q(x) · d(x)  +  R(x)

   donde:  D(x)  →  dividendo
            d(x)  →  divisor
            Q(x)  →  cociente
            R(x)  →  residuo
```

Es el mismo principio que en la división de números, pero trabajando con potencias de x.

**Desarrollo (pasos).** (1) Ordenar de mayor a menor grado. (2) Dividir términos líderes → término del cociente. (3) Multiplicar el divisor por ese término. (4) Restar al dividendo o resto parcial. (5) Repetir hasta que el resto tenga grado menor que el divisor. (6) Resultado: cociente + residuo/divisor.

**Excepciones.** Divisor cero: no definido. Grado de D menor que d: Q = 0, R = D. Divisor constante: dividir cada coeficiente. Faltan términos: usar 0. Ruffini solo para (x − a).

**Cierre.** El método sirve para factorizar y para el teorema del residuo; si el procedimiento es correcto, el residuo lo confirma.

---

## Versión extendida (referencia)

### Preguntas previas

**¿A quién está dirigido este documento?**  
A estudiantes de secundaria o primeros cursos universitarios que ya manejan suma, resta y multiplicación de polinomios y necesitan un procedimiento claro para dividirlos.

**¿Qué idea desea transmitir al lector?**  
Que la división de polinomios es un proceso ordenado y repetitivo, análogo a la división aritmética: siempre se obtiene cociente + residuo, y el residuo tiene grado menor que el divisor (o es cero).

**¿Qué conocimientos previos debe tener el lector?**  
Ordenar términos por potencias descendentes; identificar término líder (mayor exponente); sumar, restar y multiplicar polinomios; saber que x⁰ = 1 y que un término ausente equivale a coeficiente 0.

---

### INICIO (3–4 líneas)

La división de polinomios permite expresar la relación entre dividendo, divisor, cociente y residuo mediante la **fórmula fundamental**:

```
        D(x)  =  Q(x) · d(x)  +  R(x)

   donde:  D(x)  →  dividendo
            d(x)  →  divisor   (d(x) ≠ 0)
            Q(x)  →  cociente
            R(x)  →  residuo    (grado de R < grado de d, o R = 0)
```

El objetivo del método es hallar Q(x) y R(x) de forma sistemática, como en la división aritmética, pero con potencias de x.

---

### DESARROLLO — Método de división larga (pasos)

**Paso 0.** Ordenar dividendo y divisor de mayor a menor exponente. Completar con 0 los términos que falten.

**Paso 1.** Dividir el término líder del dividendo (o del resto parcial) entre el término líder del divisor. El resultado es un término del cociente.

**Paso 2.** Multiplicar todo el divisor por ese término del cociente.

**Paso 3.** Restar ese producto del dividendo (o del resto parcial), alineando términos semejantes. Obtienes un nuevo resto parcial.

**Paso 4.** Repetir los pasos 1–3 con el resto parcial como nuevo dividendo, hasta que el grado del resto sea menor que el grado del divisor.

**Paso 5.** Escribir el resultado:

dividendo ÷ divisor = cociente + (residuo ÷ divisor)

o bien: D(x) = Q(x)·d(x) + R(x)

**Ejemplo breve:**  
(x² + 5x + 6) ÷ (x + 2) = x + 3, residuo 0.

---

### EXCEPCIONES Y casos especiales

- **Divisor nulo** (d(x) = 0): la división no está definida.
- **Grado del dividendo menor que el del divisor**: cociente Q(x) = 0 y residuo R(x) = D(x).
- **Divisor constante** (grado 0): dividir cada coeficiente del dividendo entre ese número.
- **Términos faltantes**: escribir coeficiente 0 (ej. x³ + 1 como x³ + 0x² + 0x + 1).
- **División sintética (Ruffini)**: solo si el divisor es lineal, de la forma (x − a); no sirve para divisores cuadráticos sin adaptación.

---

### CIERRE (2–3 líneas)

La división sirve para factorizar, simplificar fracciones algebraicas y aplicar el teorema del residuo (al dividir entre x − a, el residuo vale R(a) = D(a)). Si se respetan el orden y los pasos, el método es reproducible y el residuo confirma si la división fue correcta.

---

## Nota

Copia el texto en la hoja con notación habitual (x², fracciones). La foto del manuscrito la debes tomar y subir tú al aula virtual.
