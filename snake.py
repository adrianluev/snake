from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)       #Crea un vector en el origen
snake = [vector(10, 0)]   #Crea una matriz donde almacenaremos las posiciones 
aim = vector(0, -10)      #Crea un vector

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):         #Funcion para confirmar si la cabeza toca la frontera del mapa
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190 
    #regresa el valor logico que cumple con un rango de -200 a 190 en X y de -200 a 190 en Y


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0) #Tamaño de pantalla(x,y) y 
hideturtle()            #Esconde el apuntador de posicion (flecha)
tracer(False)           #Desactiva la animacion de trazado que solo debe activarse al final
listen()                #Empieza la sensible captación de inputs
onkey(lambda: change(10, 0), 'Right')    #Cambio de dirección por comando de flecha "derecha"
onkey(lambda: change(-10, 0), 'Left')    #Cambio de dirección por comando de flecha "izquierda"
onkey(lambda: change(0, 10), 'Up')       #Cambio de dirección por comando de flecha "arriba"
onkey(lambda: change(0, -10), 'Down')    #Cambio de dirección por comando de flecha "abajo"
move()                  #Funcion move()
done()
