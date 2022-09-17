from random import randrange
import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
AZUL = '\033[34m'
RESET = '\033[39m'

#Arreglo de jugadores
jugadores = []

#Bool
jugar = True

#Condicion
while jugar == True:
  print (AZUL+"\nBienvenido a mi trivia sobre preguntas random"+RESET)
  time.sleep(2)
  print ("Comenzaremos con las preguntas random")
  time.sleep(2)
  
#Puntaje random al comenzar
  puntaje = random.randint(1, 10)

#Print de jugadores
  jugador1 = input ("Ingresa el nombre del jugador 1: ").upper()
  jugador2 = input ("Ingresa el nombre del jugador 2: ").upper()
  print("------------------------")

  #Agregamos los jugadores a la lista
  jugadores.append(jugador1)
  jugadores.append(jugador2)
  # escoger aleatoriamente al jugador
  i = randrange(len(jugadores))
  lista = jugadores[i].upper()
  
  #Bienvenida al jugador
  time.sleep(2)
  print(RED+"Instrucciones","\n Cada punto correcto vale 10 puntos\n Cada punto incorrecto son -5 puntos")
  time.sleep(4)
  print("\nEspera a que el contador pare para escribir tu respuesta")
  time.sleep(4)
  print("Se escogera al jugador y los puntos de forma aleatoria, suerte!"+RESET)
  time.sleep(3)
  #Mostramos al jugador random
  print(YELLOW+"Se escogio aleatoriamente al jugador: "+RESET, BLUE+jugadores[i]+RESET)
  time.sleep(5)
  print("\n Hola", YELLOW+jugadores[i]+RESET, "responde las preguntas escribiendo la letra de la alternativa y presiona 'Enter' para enviar tu respuesta:\n")

 

  time.sleep(3)
  #Mostramos el punto random del jugador
  print(YELLOW+"\nSe escogio aleatoriamente los puntos y al jugador:\n", BLUE+jugadores[i]+RESET,YELLOW+"\n => ",puntaje, "Puntos"+RESET)

  time.sleep(3)
  print("\n")
  print(MAGENTA+"-----------------BIENVENIDO------------------"+RESET)

  #Lista de las preguntas
  letras = ["a.","b.","c.","d."]
  #Respuestas
  respuestas = ["Iphone 14","Iphone 12","Iphone 13","Iphone 11 PRO MAX\n"]
  
  # Pregunta 1
  time.sleep(3)
  print (BLUE+"\n1) ¿Cual es el ultimo iphone que lanzo apple?\n"+RESET)

  time.sleep(2)
  #Recorremos las letras y respuestas
  for number in range(0,4):
    print(letras[number], respuestas[number])
  #print (GREEN+"\na) Iphone 13")
  #print ("b) Iphone 14")
  #print ("c) Iphone 12")
  #print ("d) Iphone 11 PRO MAX"+RESET)
  
  #print("\nResponde en")
  #Agregamos un tiempo de 3s para que el usuario responda
  #for numero in range (3,0,-1):
   # print(numero)
  time.sleep(2)
  print(YELLOW+"Jugador: ", jugadores[i], "esta jugado"+RESET)
  # Guardamos la respuesta en un variable"
  respuesta_low = input("\nTu respuesta: ")
  time.sleep(2)
  
  #Convertir respuesta a minuscula
  respuesta = respuesta_low.lower()

  #Ponemos una condicion de validacion
  while respuesta not in ("a", "b", "c", "d"):
    respuesta = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  #Validamos si escogi la respuesta correcta
  if respuesta == "a":
    puntaje += 10
    print(YELLOW+"Muy bien!, ganaste 10 puntos sigue jugando")
    print("Puntaje total:"+RESET, puntaje)
    
   #Si no escogio la respuesta correcta se lo mostramos
  else:
    puntaje -= 5
    print(YELLOW+"Incorrecto!! Perdiste 5 puntos!")
    print("Puntaje total:", puntaje)
    print(""+RESET)
  #PREGUNTA 2
    #-----------------------------------------------------------
  #Creamos una lista
  letras2 = ["a.","b."]
  respuestas2 = ["Verdadero","Falso"]

  #Pregunta
  time.sleep(3)
  print (BLUE+"\n2) El mejor amigo de Bob Esponja es Patricio Estrella. Verdader o falso?\n"+RESET)
  time.sleep(2)
  #Recorremos las letras y respuestas
  for number in range(0,2):
    print(letras2[number], respuestas2[number])
  
  
  #print("\nResponde en")
  #tiempo
  #for numero in range (2,0,-1):
   # print(numero)
  time.sleep(2)
  print(YELLOW+"\nJugador: ", jugadores[i], "esta jugado"+RESET)
  # Guardamos la respuesta en una variable "
  respuesta_low = input("\nTu respuesta: ")
  time.sleep(2)
  #Convertir respuesta a minuscula
  respuesta = respuesta_low.lower()

  #Validacion
  while respuesta not in ("a", "b"):
    respuesta = input("Debes responder a o b. Ingresa nuevamente tu respuesta: ")

  #Evaluamos la respuesta correcta
  if respuesta == "a":
    puntaje += 10
    print(YELLOW+"Muy bien!, ganaste 10 puntos sigue jugando")
    print("Puntaje total:", puntaje)
    print(""+RESET)
  else:
    puntaje -= 5
    print(YELLOW+"Incorrecto!, Perdiste 5 puntos!")
    print("Puntaje total:", puntaje)
    print(""+RESET)
  #PREGUNTA 3
    #-----------------------------------------------------------
  #Creamos una lista
  letras3 = ["a. ","b. ","c. ","d. ","e. "]
  respuestas3 = ["Leonardo DiCaprio","Sigmund Freud","Miguel Angel","Francesco del Giocondo","Leonardo da Vinci"]

  #Pregunta3
  time.sleep(3)
  print (BLUE+"\n3) ¿Quien pinto la monalisa?\n"+RESET)
  time.sleep(3)
  for number in range(0,5):
    #recorremos la lista y la mostramos
    print(letras3[number], respuestas3[number])
  
  
  
  #print("\nResponde en")
  #for numero in range (2,0,-1):
   # print(numero)
  time.sleep(2)
  print(YELLOW+"\nJugador: ", jugadores[i], "esta jugado"+RESET)
  # Almacenamos la respuesta del usuario en la variable "respuesta"
  respuesta_low = input("\nTu respuesta: ")
  time.sleep(2)
  #Convertir respuesta a minuscula
  respuesta = respuesta_low.lower()
  
  while respuesta not in ("a", "b","c","d","e"):
    respuesta = input("Debes responder a, b, c, d, e. Ingresa nuevamente tu respuesta: ")
  
  if respuesta == "e":
    puntaje += 10
    print(YELLOW+"Muy bien!, ganaste 10 puntos sigue jugando")
    print("Puntaje total:", puntaje)
    print(""+RESET)
   
  else:
    puntaje -= 5
    print(YELLOW+"Incorrecto!, Perdiste 5 puntos!")
    print("Puntaje total:", puntaje)
    print(""+RESET)
  
  #-------------------------------------------------------
  # Pregunta 4
  respuestas4 = ["Francia","Italia","Holanda","España"]
  time.sleep(3)
  print (AZUL+"\n4) ¿En qué país se encuentra la Torre Eiffel?\n"+RESET)
  time.sleep(3)
  for number in range(0,4):
    print(letras[number], respuestas4[number])
  
  #print("\nResponde en")
  #for numero in range (3,0,-1):
   # print(numero)
  time.sleep(2)
  print(YELLOW+"\nJugador: ", jugadores[i], "esta jugado"+RESET)
    
  respuesta_low = input("\nTu respuesta: ")
  time.sleep(2)
  #Convertir respuesta a minuscula
  respuesta = respuesta_low.lower()
  
  while respuesta not in ("a", "b", "c", "d"):
    respuesta = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error

  time.sleep(2)
  if respuesta == "a":
    puntaje += 10
    print (YELLOW+"Muy bien!, ganaste 10 puntos")
    print("\nPuntuacion total:", puntaje, "gracias por jugar"+RESET)
  
  else:
     puntaje -= 5
     print (YELLOW+"Incorrecto!, Perdiste 5 puntos, La torre Eiffel se encuentra en francia")
     print("\nPuntuacion total", puntaje, "gracias por jugar"+RESET)
     print("")
  #Creamos un bonus de puntos que puede ganar escribiendo ruleta
  time.sleep(2)
  bonus = input(YELLOW+"\nEscribe ruleta para obtener un bonus de puntos aleatorio "+RESET).lower()

   #Si no escribe correctamente se le mostrara al usuario
  while bonus not in ("ruleta"):
    bonus = input("No escribiste correctamente, intenta nuevamente").lower()

      #Si escribio ruleta se le asigna puntos random
  if bonus == "ruleta":
    bono = random.randint(0, 20)
    print(BLUE+"Felicidades\n  => Jugador:  ",jugadores[i], "ganaste" ,bono, "puntos de bono"+RESET)
    print(YELLOW+"--------FIN DEL JUEGO------------"+RESET)
    print(YELLOW+" => Total de puntos: ", bono + puntaje)
    print("")
    
    #Preguntamos si quiere seguir jugando
  game = input("Deseas continuar jugando? Responde si o no\n").lower()

  while game not in ("si", "no"):
    game = input("No escribiste correctamente, intenta nuevamente").lower()
     
#Si escribe si, sigue jugando
  if game != "si":
      print("Gracias por jugar :)") 
      jugar= False
   
   
    
  
          
  