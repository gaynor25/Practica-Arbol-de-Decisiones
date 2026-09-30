 # Práctica: Árbol de Decisión
 Se utilizo 'scikit-learn' para crear un modelo de clasificación utilizando unarbol de decision.Este fue entrenado utilizando el 80% de los datos y el 20% restante para realizar pruebas.

 ### Resultados
Aqui lo que se hizo fue cambiar el valor de max_depth para asi observar como es que cambiaban las reglas y la precision del arbol.

El primer fue max_depth=2 con una precision de 86.11% de ahi fue subiendo 3, 4, 5, llegue hasta la 10 y por ultimo utilice None todos estos (3,4,5,..., None) obtuvieron una precision de 94.44%

Nos dimos cuenta que al aumenta max_depth las reglas del arbol se hicieron mas detalladas al igual que aparecieron caracteristicas adicionales como ash y alcohol en las reglas de clasificación.

### Árbol sin límite de profundidad
Al utilizar max_depth = None el arbol no tuvo un limite establecido de profundidad. 

Gracias a esto nos dimos cuenta de que el arbol alcanzo una profundidad real de 4.

Esto muestra que al aumentar la profundidad no siempre significa obtener una mayor precisión.

### Resultados opinión
Pienso que los resultados fueron buenos porque el modelo logro una precisión del 94.44% en los datos de prueba.

Tambien se puede observar que despues de cierta profundidad la precision dejo de aumentar (se agregaban mas reglas pero la precisión no aumentaba).

### El dataset cumple con los requerimientos?
Si, el dataset cumple con los requerimientos para utilizarse en un modelo de árbol de decisiones ya que este contiene diferentes características numéricas de los vinos y una variable de clase que permite que estos se clasifiquen en diferentes grupos.

Agregando que las caracteristicas pueden utilizarse para realizar divisiones y crear reglas que permitan clasificar de mejor manera a los vinos.

#### Características fundamentales ¿Por qué? ¿Qué mas agregarias?
Pensaria que estan son las caracteristicas importantes
* color?intensity
* ash
* proline
* alcohol
Se utilizaron dentro del árbol para realizar diferentes divisiones y determinar la clase de cada vino.

### Conclusión
Con esta práctica se observó como es que funciona un árbol de decisión y cómo cambia al modificar su profundidas.
Se comprobó que una mayor profundidad genera reglas más detalladas, pero no necesariamente aumenta la precisión del modelo.

