[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Y59lTQr6)

[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23693765)


#Juego con premio para gatito 

Este simulador en Python que armé para el trabajo en clase de Monty Hall, usamos: un gato buscando su comida.


#Como es:

El escenario es:Hay 3 cajas. Dos tienen un pepino (el terror de los michis) y una tiene un pescadoEl gato elige una caja al azar.El humano que sabe las posiciones abre una de las otras cajas y muestra un pepino.Ahora el gato tiene una elección: ¿Se queda con su caja o cambia a la otra que queda cerrada? 


#El Código

El script corre miles de simulaciones para comparar dos estrategias:play_stay: El gato es testarudo y se queda con su elección  inicial play_change: El gato se asusta del pepino y salta a la otra caja.Usé la librería random (específicamente random.choice) para manejar las decisiones del gato y del humano. Solo necesitas Python 3 y ejecutar el main:Bashpython gato_monty.py
Aunque parezca que da igual, la estadística dice que el gato es más listo si cambia de caja.Si se queda: Gana solo el $33\%$ de las veces.Si cambia: ¡Gana el $66\%$ Si cambias, estás aprovechando la información que el humano te dio al enseñarte dónde estaba uno de los pepinos.

 Autor: [José de Jesús Hernández Coutiño]
 
 Fecha: Abril 2026
