#importamos libreria turtle es una herramienta 
#gráfica sencilla que permite crear dibujos, 
#gráficos y animaciones de forma visual.
from cgitb import text
import turtle
#importamos ramdon
import random
#para retrasar
import time
posponer = 0.1

#Marcador
score = 0
high_score = 0

# configuracion de la ventana
wn = turtle.Screen()

wn.title("Juego de la serpiente ")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Cuerpo de la serpiente
segmentos = []

#Texto para el marcador o totalScore
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("  Score: 0       High Score: 0 ", align = "center", font=("Courier", 24, "normal"))


#funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"



def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
        
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        
#teclado, le vamos a otorgar conexion al juego con el teclado
wn.listen()        
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

#Ciclo que le da un tiempo finito al programa
while True:
    #colisiones bordes
    if cabeza.xcor()> 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:  
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza. direction = "stop"
        
        #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(10000, 10000)
            
        #Limpiar la lista de los segmentos
        segmentos.clear()
        
        #Resetear marcador
        score = 0
        texto.clear()
        texto.write("Score: {}        High Score{}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))

    wn.update()
    #colisiones comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        
        #AUMENTAR MARCADOR
        score +=10
        
        if score > high_score:
            high_score = score
            
        texto.clear()    
        texto.write("Score: {}      High Score{}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))
        
    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range (totalSeg - 1, 0 , -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)
        
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
        
    
        
    mov()
    
    #colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            #esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
                
            segmentos.clear()
            #Resetear marcador
            score = 0
            texto.clear()
            texto.write("Score: {}        High Score{}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))


    time.sleep(posponer)



# sirve para que el comando turtle no cierre la pestaña, sino que la mantenga abierta
turtle.done()
