from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
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
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
