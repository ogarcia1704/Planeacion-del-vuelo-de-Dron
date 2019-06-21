# Planeacion-del-vuelo-de-Dron
Oswaldo Missael García Orozco, Sebastián George Heredia
P.E. Ingeniero Topógrafo Geomático, Facultad de Ingeniería Civil, Universidad de Colima, Campus Co-quimatlán, Coquimatlán, Colima, 28400, ogarcia@ucol.mx, sgeorge@ucol.mx

Resumen

Una Buena planificación de vuelo es, con diferencia, el factor que tiene la mayor in-fluencia en la calidad de los resultados, y su programación para la planificación de dicho vuelo.

Palabras clave: Dron, coordenadas, planifica-ción, vuelo, programación.

Abstract

A good flight planning is, with the difference, the factor that has the greatest influence on the quality of the results, and its propagation for the planning of that flight.

Keywords:  Drone, coordinates, planning, flight, programming. 

Introduccion

En este programa se llevará a cabo el planea-miento de vuelo de un dron por medio de la fotogrametría. Lo llevaremos a cabo por medio de diferentes factores, ya sea la dimensión por medir, las condiciones climáticas, el tipo de cámara de nuestro dron, etc.
Por medio de fórmulas de fotogrametría noso-tros podremos sacar que tanto va a abarcar nuestra imagen de acuerdo a los factores ya mencionados.
La fotogrametría es la ciencia o técnica cuyo objetivo es el conocimiento de las dimensiones y posición de objetos en el espacio, a través de la medida o medidas realizadas a partir de la intersección de dos o más fotografías, o de una fotografía y el modelo digital del terreno co-rrespondiente al lugar representado, el cual ha de ser realizado anteriormente por intersección de dos o más fotografías.
Por lo que resulta que el concepto de fotogra-metría es: "medir sobre fotos".
Si trabajamos con una foto podemos obtener información en primera instancia de la geometría del objeto, es decir, información bidimensional. Si trabajamos con dos fotos, en la zona común a éstas (zona de solape), podremos tener visión estereoscópica; o dicho de otro modo, infor-mación tridimensional.
Esta técnica es básica para la elaboración de toda la cartografía, ya sea topográfica, temáti-ca, catastral, etc.
Puede ayudarse de información espectral y radiométrica de una imagen digital apoyada en la teledetección.
La fotogrametría puede ser terrestre o aérea dependiendo desde donde son obtenidas las imágenes

Desarrollo

Los drones son aeronaves no tripuladas que se controlan de forma remota y se utilizan para diferentes tipos de misiones o tareas.
Los drones sirven para muchas tareas y activi-dades actualmente, tienen la capacidad de aho-rrar tiempo, costos y recursos dependiendo su tipología.
Existen Drones tipo multirrotor, otros Ala Fija o Helicópteros; la importancia de diferenciar cada uno es clave para sacar el mayor provecho para el trabajo que deseas realizar, ya que estas son herramientas extremadamente útiles, por ejem-plo, para agricultura, construcción, atención de emergencias y desastres, control de tráfico, topografía y más; pero el uso que se le puede dar a un Drone no son sólo operaciones a gran escala o industriales.
¿Qué tipo de trayectoria debería cubrir el dron? ¿Cuántas fotos son necesarias? ¿A qué altura? Una buena planificación del vuelo es, con dife-rencia, el factor que tiene la mayor influencia en la calidad de los resultados a la hora de generar mapas 2D y reconstrucciones 3D.
Hay tres aspectos que son claves a la hora de realizar fotogrametría con drones:
1.	La trayectoria de vuelo
2.	El solape entre las imágenes.
3.	Posición de la cámara.
Estos tres elementos vienen determinados por una necesidad común: para que un detalle sea fielmente reconstruido, es necesario que apa-rezca en un número mínimo de fotografías. Cuanto más variados y numerosos sean los puntos de vista, más abundancia de informa-ción útil a la hora de hacer el procesado. Anali-zaremos diferentes escenarios y el plan de vue-lo fotogramétrico recomendado para cada ca-so.
La trayectoria a seguir será la de forma de cua-drícula (Figura 1.1). Los solapes mínimos son entre 75% (frontal) y al menos el 60% (lateral). La posición de la cámara estará totalmente per-pendicular apuntando al suelo (plano cenital).
 
 Figura 1.1 (Planificación de vuelo para la gene-ración de un mapa)
Planificación de vuelo de canteras y áreas cons-truidas
Tanto para generar reconstrucciones en 2D co-mo 3D es básico disponer de varios puntos de vista alternativos para cada área. Por ello, es necesario completar una trayectoria de doble cuadrícula, es decir, completar una trayectoria como para el caso de una ortofoto y continuar con otra semejante a 90 grados (Figura 1.2). Con este tipo de trayectoria nos aseguramos de tener fotografías desde cuatro puntos (aproxi-mados) norte, sur, este y oeste. El solape, igual que en el caso anterior, 75% y 60%.
Para que las paredes verticales puedan ser re-construidas, es necesario que la cámara apunte en un ángulo de entre 10º y 35º.
  
Figura 2.1 (Planificación de vuelo de áreas construidas)
Planificación de vuelo para generar volúme-nes 3d (edificios, estructuras verticales…)
Es necesario completar tres trayectorias circula-res a diferentes alturas, en un único vuelo o en varios vuelos consecutivos.
La cámara debe formar un ángulo de 45º en la trayectoria más baja, 30º en la media y 10º en la más elevada (Figura1.3). Es necesario tomar entre 40 y 80 capturas en cada una de las órbi-tas, es decir, cada foto estará separada de la anterior por 5º – 10º grados. En todos los ca-sos, la cámara debe tomar como punto de inte-rés el centro aproximado del objeto.
  
Figura 3.1 (Planificación de vuelo para volúme-nes 3d)
En el caso de objetos muy grandes es necesa-rio modificar estos valores de forma que siga existiendo la misma cantidad de solape entre imágenes. En este caso, más fotos, cada me-nos grado y si el objeto es muy alto, añadiendo progresivamente más órbitas.
Ante todo, evitar incluir la línea del horizonte, el cielo o el sol en las fotografías. Un set de fotos en el que aparezcan es un buen candidato para problemas durante reconstrucción. Nuestro equipo tiene capacidad para arreglarlas, pero este es un proceso manual.
Otro elemento importante, al orbitar alrededor del objeto, la posición del sol va a cambiar radicalmente, con lo que tendréis fotografías de zonas en sombra con otras totalmente ilumina-das. En algún caso, determinadas zonas pue-den estar subexpuestas y otras sobreexpues-tas. Si no hay unos parámetros de cámara que permitan utilizar una exposición fija, utilizad exposición automática. Nuestro software es capaz de utilizar ambos casos.
¿Qué hacer si tu escena no se ajusta perfecta-mente a ninguno de los casos anteriores? No hay problema. Si es una combinación de áreas planas y edificaciones bajas, completad un vuelo semejante descrito en segundo lugar. Si es una estructura vertical en medio de una zona plana, utilizad el primer y tercer caso.
Dada la información que podremos generar con un simple dron, uniremos el lenguaje Python para que nos genere la información que quere-mos encontrar, generando códigos y librería para la obtención de dichos datos,.

Manejo de datos

Para la realización de este programa, utilizamos un programa de programación visto en clases el cual es Python 2.7 y 3.7, cabe descargar que para tener estos programas necesitamos una computadora para tener manejo de ellos, noso-tros utilizamos la HP Pavilon, con un sistema operativo de 64 bits, con procesador x64, con una memoria RAM de 12 gb, y Windows 10.

Resultados

Los resultados aplicados en este programa no fueron los deseados como esperábamos, pero pudimos encontrar mejoras en lo que llevába-mos haciendo a lo largo de esta ultima parcial, pudimos obtener las características de una ima-gen dada, esto ayuda bastante ya que de ahí podemos generar bastantes cosas acerca de ella, además como convertir todas esas carac-terísticas en un archivo xlsx (Excel), esto para que dentro de esta planilla puedas hacer los cálculos necesarios para poder sacar, áreas, perímetros, tiempos, además de que ya tenien-do las características e un archivo Excel sea mas fácil manipular los datos correspondientes, dado esto podemos generar otros logaritmos que nos puedan ayudar para otros problemas externos al el vuelo de un dron.

Conclusiones

Sebastián George Heredia.
En conclusión este programa que hemos esta-do trabajando a lo largo de la tercer parcial nos dejo muy en claro que es complicado, ya que tienes que tener buen conocimiento y para ello debes investigar, indagar, observar y utilizar la información mas importante que te pueden ayu-dar para tener un mejor desempeño en tu pro-grama, además, de las librerías necesarias den-tro de Python para poder efectuar las aplicacio-nes que quieres que ejerza dicho logaritmo, consecuente podemos analizar de manera logís-tica que lo obtenido en el programa fue al estu-dio y desempeño de cada clase, además del apoyo de nuestro profesor para el desarrollo de dicho programa, es importante saber todo acer-ca de tu tema para tener una mejor idea de lo que quieres lograr, la programación es muy importante e interesante, espero que nuestro programa pueda llegar a un buen alcanza y di-cho el tiempo poder seguir mejorándolo día con día, para un futuro tener mejor precepción de lo que queremos ser.
Oswaldo Missael García Orozco
Este programa hecho por mí y mi compañero fue un claro ejemplo de lo que realizamos en esta tercera parcial lo cual lo aplicamos a nues-tra vida cotidiana para facilitarnos nuestra vida profesional la cual lo vamos a tener que aplicar en nuestra vida profesional, porque mientras mas rápido y bien hagas tu trabajo mejor será tu desempeño como profesionista y será mejor pagado.
Con la ayuda de este programa también hicimos mucho hincapié en el estudio de la fotograme-tría que es una rama muy importante para la Topografía, la cual es el estudio de imágenes áreas y este programa fue un claro ejemplo de eso.

Referencias

https://www.aerial-insights.co/blog/como-planificar-capturas-de-dron/

https://norbertrovira.com/python-y-drones/

https://github.com/dronekit/dronekit-python 





![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/ogarcia1704/Planeacion-del-vuelo-de-Dron/master/1.png)
![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/ogarcia1704/Planeacion-del-vuelo-de-Dron/master/2.png)
![PalabrasdelTextoAlternativ](https://raw.githubusercontent.com/ogarcia1704/Planeacion-del-vuelo-de-Dron/master/3.png)
