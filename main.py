
###todo Recursos

##* Import
import random
import time

##* Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
NORMALIZE = '\033[39m'

##* lista de opciones
listaOpciones = ["a", "b", "c", "d"]

##* Preguntas
pregunta_p1 = "\n¿Quién fue campeón de la Fórmula 1 2021?"
pregunta_p2 = "\n¿Qué escudería lidera el Campeonato de Constructores este año?"
pregunta_p3 = "\n¿Qué es un ‘safety car’?"
pregunta_p4 = "\n¿Cuántos Campeonatos Mundiales de pilotos tiene Lewis Hamilton?"
pregunta_p5 = "\n¿Cuáles son las siglas de la máxima autoridad del automovilismo, incluyendo la Fórmula 1?"
pregunta_p6 = "\n¿Cuál es(son) la(s) escudería(s) más antigua(s) que aún compite en la Fórmula 1?"

##* Alternativas
alternativas_p1 = [
    "a) Lewis Hamilton", 
    "b) Valtteri Bottas", 
    "c) Max Verstappen",
    "d) Sergio “Checo” Perez"
]
alternativas_p2 = [
    "a) Ferrari", 
    "b) Red Bull Racing", 
    "c) Mercedes-AMG",
    "d) McLaren"
]
alternativas_p3 = [
    "a) El auto que lleva al ganador al podio",
    "b) El coche que lidera al inicio de la carrera",
    "c) El coche de seguridad en la pista",
    "d) El coche más rapido de la pista"
]
alternativas_p4 = [
    "a) 4 títulos", 
    "b) 3 títulos", 
    "c) 1 títulos",
    "d) 7 títulos"
]
alternativas_p5 = [
  "a) FIA", 
  "b) AFI", 
  "c) IFA",
  "d) FIIA"
  ]
alternativas_p6 = [
    "a) McLaren y Ferrari", 
    "b) Ferrari", 
    "c) McLaren", 
    "d) Ferrari, McLaren y Williams"
]

##* Opciones True
opcionTrue_p1 = "c"
opcionTrue_p2 = "b"
opcionTrue_p3 = "c"
opcionTrue_p4 = "d"
opcionTrue_p5 = "a"
opcionTrue_p6 = "b"

##* Puntaje
puntajeIntento = 0
puntajeCorrecto = 100
puntajeExtra = 0
puntajeIncorrecto = 50

##* Funcion para cada pregunta
def preguntas(param_pregunta, param_alternativas, param_opcionTrue):

  #* Imprime las preguntas y alternativas
  print(param_pregunta)
  for iteracion in param_alternativas:
      print(iteracion)

  #* Bucle de respuesta incorrecta
  while True:
    global puntajeIntento
    variable = input(CYAN + "Introduzca la opción correcta: ")
    variable = variable.strip()
    variable = variable.lower()

    ##* Verificar letra dentro de alternativas
    while variable not in listaOpciones:
      variable = input(CYAN + "Introduzca una letra dentro de las opciones mostradas: ")
      variable = variable.strip()
      variable = variable.lower()

    ##* Verificar respuesta correcta
    if variable != param_opcionTrue:
      print(RED + "No es la respuesta correcta, inténtalo otra vez")
      puntajeIntento = puntajeIntento - puntajeIncorrecto
      print(YELLOW + f"\nTu puntaje actual es: {puntajeIntento}" + NORMALIZE)

    else:
      print(GREEN + "Excelente, es la respuesta correcta")
      puntajeIntento = puntajeIntento + puntajeCorrecto
      print(YELLOW + f"\nTu puntaje actual es: {puntajeIntento}" + NORMALIZE)
      break

  return



###todo Bienvenida de Trivia
###todo Bienvenida de Trivia
###todo Bienvenida de Trivia
# print(YELLOW + "Trivia de Fórmula 1" + NORMALIZE)

# time.sleep(1)
# nombreParticipante = input(MAGENTA + "¿Cuál es tu nombre? " + NORMALIZE)
# if nombreParticipante == "Admin":
#   print(MAGENTA + "Bienvenido usuario curioso, espero que éstas preguntas puedan ser de tu agrado" + NORMALIZE)
#   print("En agradecimiento, te añadiremos 100 puntos extra en tu score")
#   puntajeExtra = 100
# else:
#   print(YELLOW + f"Bienvenido {nombreParticipante}\nAplica tus conocimientos y obtén el máximo puntaje. ¡Vamos!")



##* Suerte aleatoria en puntajes
# time.sleep(3)
# suerte = input("\n¡Espera un momento! ¿Te gustaría que la Suerte ingrese en esta trivia? (Si/No) ")
# suerte = suerte.lower()

# if suerte == "si":
#   print("La suerte se está preparando, espere...")
#   time.sleep(3)
#   print("\n¡La Suerte está dentro!, esperemos que obtengas el mayor puntaje en este intento...")
#   puntajeCorrecto = random.randint (11, 100)
#   print(f"Además, la Suerte dictaminó que en este intento, por respuesta correcta tendrás +{puntajeCorrecto} puntos. Empecemos a jugar...")

# else:
#   print(f"La Suerte no está invitada en este intento. Tu puntaje por respuesta correcta será +{puntajeCorrecto}. Empecemos a jugar...")
# time.sleep(2)



# print()
# ##* Carga inicial de 5 segundos
# for numero in range(5, 0, -1):
#   print(numero)
#   time.sleep(1)


##* Bucle intentos
intento = 1
repetir = True
while repetir == True:
  puntajeIntento = 0

  ##* Puntaje inicial
  print(YELLOW + f"\nTu puntaje inicial es: {puntajeIntento}" + NORMALIZE)
  time.sleep(2)


  ##* Preguntas

  preguntas(pregunta_p1, alternativas_p1, opcionTrue_p1)
  time.sleep(2)

  preguntas(pregunta_p2, alternativas_p2, opcionTrue_p2)
  time.sleep(2)

  preguntas(pregunta_p3, alternativas_p3, opcionTrue_p3)
  time.sleep(2)

  preguntas(pregunta_p4, alternativas_p4, opcionTrue_p4)
  time.sleep(2)

  preguntas(pregunta_p5, alternativas_p5, opcionTrue_p5)
  time.sleep(2)

  preguntas(pregunta_p6, alternativas_p6, opcionTrue_p6)
  time.sleep(2)


  ##* Carga aleatoria final
  numeroAleatorio = random.randint(3, 5)
  for carga in range(numeroAleatorio, 0, -1):
    print(carga)
    time.sleep(1)



  print(YELLOW + "\nFelicidades, terminaste la Trivia de Fórmula 1.")
  print(MAGENTA + f"Tu puntaje Final es: {puntajeIntento + puntajeExtra}")

  preguntaNuevoIntento = input(MAGENTA +"¿Quieres intentarlo de nuevo? (Si/No) ")
  suerte = suerte.lower()
  if preguntaNuevoIntento == "no":
    break
  else:
    intento +=1

print(f"\nTu número de intentos fue: {intento}" + NORMALIZE)
