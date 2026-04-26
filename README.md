Este proyecto consiste en el desarrollo y aplicación de herramientas computacionales para el análisis y solución de problemas de ingeniería relacionados con el esfuerzo normal en elementos elongados sometidos a flexión. El objetivo es automatizar el cálculo de esfuerzos en secciones transversales complejas mediante el lenguaje de programación Python

Integrantes:
González López, Meyli Y.; 
Herrera Bolaina, Sergio. ;
Ramos Ventura, Alan.;
Sánchez Romero, Daniel.

Contexto del problema:

Se analiza una barra elongada de 80 cm de longitud con diferentes configuraciones de sección transversal (Caso "a": Sección L, Caso "b": Sección I, y Caso "c": Sección Circular Hueca). Estos elementos están sometidos a momentos flexionantes combinados ($M_x = 100 Nm$ y $M_y = 50 Nm$), lo que genera esfuerzos de tensión y compresión que deben ser calculados con precisión sobre el centroide de la sección compuesta

Funcionamiento del Código:

Presenta al usuario el propósito del programa y los casos disponibles.

Solicita las dimensiones geométricas de la sección (como base, altura, espesor o radios) en metros.

Calcula los momentos de inercia (I_x, I_y) y aplica la fórmula del esfuerzo normal total para puntos críticos de la geometría

Muestra en pantalla el valor del esfuerzo normal total en Pascales (Pa) e indica si el punto se encuentra bajo tensión o compresión.
