# Teoria-cuantica-basica
En la libreria 04 encontraremos operaciones como:
#
1. Calcular la probabilidad de encontrar un sistema en una posición en particular.

2. Buscar la probabilidad de transitar de un primer vector ket al segundo.

3. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación

4. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.

5. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.

6. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.

# Ejercicios
4.3.1: El programa calcula el observable de una matriz con un vector y halla sus valores y vectores propios y calcula si el sistema colapsa en un vector propio

4.3.2: Con los vectores propios anteriores, el programa calcula la probabilidad de que el sistema anterior colapse en cada uno de ellos.

4.4.1: El programa calcula si dos matrices son unitarias y de ser así realiza su producto para evaluar si tambien es unitario.

4.4.2: Haciendo uso de la función dynamic, el programa calcula el estado final de realizar la acción de la matriz dada con el vector dado el numero de clicks requerido.

# 4.5.2

Para resolver el ejercicio, debemos comenzar por comprender el concepto de spin en la mecánica cuántica. El spin es una propiedad intrínseca de las partículas subatómicas que se comporta como un momento angular. En la mecánica cuántica, el spin de una partícula se describe mediante un operador de spin.

Para un sistema compuesto por dos partículas que tienen spin, el vector de estado genérico se puede escribir como la combinación lineal de los estados base del sistema, que se obtienen a partir del producto tensorial de los estados base de cada partícula individual. En este caso, el vector de estado se escribe como:

|Ψ> = a|↑↑> + b|↑↓> + c|↓↑> + d|↓↓>

donde |↑> y |↓> representan los dos posibles valores del spin de cada partícula y los coeficientes a, b, c y d son números complejos que representan la amplitud de probabilidad de cada estado base.

Para un sistema con n partículas, el vector de estado genérico se puede escribir como la combinación lineal de los estados base del sistema, que se obtienen a partir del producto tensorial de los estados base de cada partícula individual. En este caso, el vector de estado se escribe como:

|Ψ> = a1|s1> ⊗ a2|s2> ⊗ ... ⊗ an|sn>

donde |si> representa el estado base del spin de la i-ésima partícula y los coeficientes a1, a2, ..., an son números complejos que representan la amplitud de probabilidad de cada estado base.

En resumen, para resolver teóricamente el ejercicio, debemos comprender el concepto de spin en la mecánica cuántica y cómo se describe el vector de estado de un sistema compuesto por partículas con spin. Luego, podemos escribir el vector de estado genérico para un sistema con dos partículas y generalizarlo para un sistema con n partículas. Este vector de estado contiene toda la información relevante sobre el sistema y es la descripción cuántica completa del mismo.

# 4.5.3

Se dice que un estado es separable si se puede escribir como el producto tensorial de los estados de dos o más sistemas. Es decir, si un estado puede descomponerse en la forma:

|ψ> = |a> ⊗ |b>

donde |a> y |b> son los estados de dos sistemas diferentes.

En el caso del estado dado |φ> = |x0> ⊗ |y1> + |x1> ⊗ |y1>, podemos ver que no es separable. Para ver esto, podemos intentar escribir el estado en la forma |a> ⊗ |b> y ver si se puede encontrar una solución para los estados |a> y |b>.

Supongamos que |φ> es separable, entonces:

|φ> = |a> ⊗ |b>

donde |a> y |b> son los estados de dos sistemas diferentes.

Entonces, podemos escribir:

|φ> = |a> ⊗ |b> = (a1|x0> + a2|x1>) ⊗ (b1|y1>)

Expandiendo la expresión del lado derecho, obtenemos:

|φ> = a1b1|x0>⊗|y1> + a2b1|x1>⊗|y1>

Sin embargo, esto no coincide con la forma dada de |φ>, lo cual significa que no se puede escribir como el producto tensorial de dos estados diferentes. Por lo tanto, podemos concluir que el estado dado |φ> no es separable.

En resumen, el estado |φ>=|x0>⊗|y1>+|x1>⊗|y1> no es separable ya que no se puede escribir como el producto tensorial de dos estados diferentes, lo cual implica que los sistemas están entrelazados y no pueden ser descritos de forma independiente.
