#Autores:
#Ricardo Rosas Esquivel - A00829089 & Adrián Luévanos Castillo A00827701
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)       #Crea un vector en el origen
snake = [vector(10, 0)]   #Crea una matriz donde almacenaremos las posiciones
aim = vector(0, -10)      #Crea un vector

#_______Definicion de cambio de colores_________
def colors(T):            #Funcion que regrea un color de 5 colores diferentes del rojo
    if T == True:
        a = randrange(1,6)#Un numero aleatorio es dado
        if a == 1:
            col = 'blue'  #Si el numero aleatrio es 1
        elif a == 2:
            col = 'black' #Si el numero aleatrio es 2
        elif a == 3:
            col = 'green' #Si el numero aleatrio es 3
        elif a == 4:
            col = 'gray'  #Si el numero aleatrio es 4
        else:
            col = 'yellow' #Si el numero aleatrio es 5
        return col

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
#_______________Funcion de frontera____________
def inside(head):         #Funcion para confirmar si la cabeza toca la frontera del mapa
    "Return True if head inside boundaries."
    return -220 < head.x < 190 and -210 < head.y < 190
    #regresa el valor logico que cumple con un rango de -200 a 190 en X y de -200 a 190 en Y


def move():
    global c1, c2
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    print(head.x, head.y)

    if (head == food ) :
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10 # Si la serpiente se come la comida genera una nueva
        food.y = randrange(-15, 15) * 10 #
        c1 = colors(True)       #Color de serpiente cambia al comer
        c2 = colors(True)       #Color de comida cambia al comer
       
    elif food.x >= 190:     #
        food.x -= 10        #
        snake.pop(0)        #
    elif food.y >= 190:     #
        food.y -= 10        #
        snake.pop(0)        #       Checa si la comida llego a una boundary y la regresa un lugar hacia atras
    elif food.x <= -200:    #
        food.x += 10        #
        snake.pop(0)        #
    elif food.y <= -200:    #
        food.y += 10        #
        snake.pop(0)        #

    else:
        snake.pop(0)
        food.x = food.x + randrange(-1, 1) * 10 # Mueve la comida un paso a la vez
        food.y = food.y + randrange(-1,1) * 10  #

    clear()

    for body in snake:
        square(body.x, body.y, 9, c1)

    square(food.x, food.y, 9, c2)
    update()
    ontimer(move, 100)

#_____________Inicia el juego
setup(420, 420, 370, 0) #Tamaño de pantalla(x,y) y
hideturtle()            #Esconde el apuntador de posicion (flecha)
tracer(False)           #Desactiva la animacion de trazado que solo debe activarse al final
listen()                #Empieza la sensible captación de inputs

c1 = colors(True)       #Color de serpiente
c2 = colors(True)       #Color de comida
while c2 == c1:         #Condición para tener siempre un color diferente
   c2 = colors(True)

onkey(lambda: change(10, 0), 'Right')    #Cambio de dirección por comando de flecha "derecha"
onkey(lambda: change(-10, 0), 'Left')    #Cambio de dirección por comando de flecha "izquierda"
onkey(lambda: change(0, 10), 'Up')       #Cambio de dirección por comando de flecha "arriba"
onkey(lambda: change(0, -10), 'Down')    #Cambio de dirección por comando de flecha "abajo"
move()                  #Funcion move()
done()
