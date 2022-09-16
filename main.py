print ("Bienvenido a mi trivia sobre computación")
print ("Pondremos a prueba tus conocimientos")
print ("Cada respuesta correcta tiene un valor 5 puntos")
contador = 0
nombre = input("Ingresa tu nombre: ")

print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

# Pregunta 1
print ("1) ¿Quién fue el creador de windows?")
print ("a) Linus Torvalds")
print ("b) Bill Gates")
print ("c) Mark Zuckerberg")
print ("d) Dennis Ritchie")
respuesta_1 = input("\nTu respuesta: ")
if respuesta_1 == "b":
     print("Respuesta Correcta, obtuviste 5 puntos")
     contador = 5 
else:
     print("Respuesta Incorrecta")
     contador = 0
#Pregunta 2
print ("1) ¿Quién fue el creador de facebook?")
print ("a) Linus Torvalds")
print ("b) Bill Gates")
print ("c) Mark Zuckerberg")
print ("d) Dennis Ritchie")
respuesta_2 = input("\nTu respuesta: ")
if respuesta_2 == "c":
     print("Respuesta Correcta, obtuviste 5 puntos")
     contador = contador + 5
else:
     print("Respuesta Incorrecta")
#Pregunta 3
print ("1) ¿Quién fue el creador de linux?")
print ("a) Linus Torvalds")
print ("b) Bill Gates")
print ("c) Mark Zuckerberg")
print ("d) Dennis Ritchie")
respuesta_3 = input("\nTu respuesta: ")
if respuesta_3 == "a":
     print("Respuesta Correcta, obtuviste 5 puntos")
     contador = contador + 5
else:
     print("Respuesta Incorrecta")
     
print(nombre, "Tu puntaje es de: ", contador)
