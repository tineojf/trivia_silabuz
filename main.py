
###todo Trivia


#* Import
#! Agregar

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
listaOpciones = ["a", "b", "c", "d", "e"]

##* Opciones correctas
opcionCorrecta_p1 = "c"
opcionCorrecta_p2 = "b"
opcionCorrecta_p3 = "c"
opcionCorrecta_p4 = "d"
opcionCorrecta_p5 = "a"
opcionCorrecta_p6 = "b"

##* Preguntas
pregunta_p1 = "\n¿Quién fue campeón de la Formula 1 2021?"
pregunta_p2 = "\n¿Qué escudería lidera el Campeonato de Constructores este año?"
pregunta_p3 = "\n¿Qué es un ‘safety car’?"
pregunta_p4 = "\n¿Cuántos Campeonatos Mundiales de pilotos tiene Lewis Hamilton?"
pregunta_p5 = "\n¿Cuáles son las siglas de la máxima autoridad del automovilismo, incluyendo la Fórmula 1?"
pregunta_p6 = "\n¿Cuál es(son) la(s) escudería(s) más antigua(s) que aún compite en la Formula 1?"

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
    "c) El coche de seguirdad en la pista",
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



###todo Bienvenida de Trivia
print(YELLOW + "Trivia de Fórmula 1" + NORMALIZE)

nombreParticipante = input(MAGENTA + "¿Cuál es tu nombre? " + NORMALIZE)
print(YELLOW + f"Bienvenido {nombreParticipante}\nAplica tus conocimientos y obtén el máximo puntaje. ¡Suerte!")



















