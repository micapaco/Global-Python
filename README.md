Participantes del Grupo: Paco Micaela, Carlos Gabriel y Palacios Brian

Ejemplo de pasos para poder utilizar la maquina de adn con la mutacion de Radiacion
1-Ingrese la siguiente Cadena de Caracteres(sin las comillas): "AGATCA GATTCA CAACAT GAGCTA ATTGCG CTGTTC"
2-Seleccione la opcion de "Detectar Mutaciones"

Output esperado = 
"Se detectaron mutaciones 
Hemos encontrado mutaciones verticales."

3-Seleccione la opcion "Mutar"
3-1.Seleccione la opcion "Radiacion"
3-2.Ingrese los caracteres correspondientes: "A, 0, 0, V" como en el ejemplo de abajo.

Ingrese la base nitrogenada para la mutación (A/T/C/G): A
Ingrese la fila para la mutación (0-5): 0
Ingrese la columna para la mutación (0-5): 0
Ingrese la orientación de la mutación (H/V): V
Ouput esperado =
ADN después de la mutación por radiación:
A G A T C A
A A T T C A
A A A T A T
A A G T T A
A T T G C G
C T G T T C

4-Seleccione la opcion de "Sanar"

Output esperado = 
Curando mutaciones...
ADN después de sanar mutaciones:
T G G A T G
C T C C A T
G G C C T T
C A A G T G
C A T T C A
T G A G A C

5-Seleccione la opcion de "Salir"

En este caso lo que hacemos es ingresar el ADN, luego verificamos si se esta infectado, despues lo mutamos por la Radiacion ingresando antes los datos pedidos y nos entrega una matriz con una mutacion de Adenina en fila 0 y columna 0.
En el cuarto punto lo que hacemos es sanar el ADN y verificando que no se encuentren mutaciones(Al curar el ADN se utiliza el "random", por ende no dara el mismo resultado como el mostrado en el output del punto 4)

Ejemplo de pasos para poder utilizar la maquina de adn con la mutacion de Radiacion

1-Ingrese el la siguiente cadena de caracteres(sin comillas): "AGATCA GATTCA CAATAT GAGCTA ATTGCG CTGTTC"
2-Seleccione la opcion de "Detectar Mutantes"
Output esperado = "No se encontraron mutaciones"

3-Seleccione la opcion "Mutar"
3-1.Seleccione la opcion "Radiacion"
3-2.Ingrese los caracteres correspondientes: "0, 0, 3" como en el ejemplo de abajo.
Output esperado = 
ADN después de la mutación por Virus:
T G A T C A
G T T T C A
C A T T A T
G A G T T A
A T T G T G
C T G T T T

4-Seleccione la opcion "Sanar"
Output esperado = 
Curando mutaciones...
El ADN ya estaba sano, no se realizaron cambios.

5-Seleccione la opcion "Salir"

En este caso ingresamos un ADN el cual no esta mutado, el detector nos devuelve que no hay mutaciones, despues lo mutamos con el Virus ingresando anteriormente los datos pedidos, nos entrega la matriz mutada, con la diagonal  principal infectada por la Timina y en el punto 4 sanamos el ADN.
