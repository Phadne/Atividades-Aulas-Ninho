import turtle

def quadrado(tam_lado):
    for i in range (4):
        turtle.forward(tam_lado)
        turtle.left(90)

def triangulo_equ(tam_lado):
    for i in range (3):
        turtle.forward (tam_lado)
        turtle.left(120)
        
def pentagono(tam_lado):
    for i in range (5):
        turtle.forward(tam_lado)
        turtle.left(360/5)
        
def poligno_reg(num_lados, tam_lado):
    for i in range (num_lados):       
        turtle.forward (tam_lado)
        turtle.left("360/num lados")
        
def retangulo (b,h):
        turtle.forward (b)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
        turtle.forward(b)
        turtle.left(90)
        turtle.forward(b)  

def f (b,h):  
    for i in range (2):
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
        turtle.forward(b)       

def daphne(b,h):
        for i in range (5):
            turtle.left(45)
            turtle.forward(h)
            turtle.left(45)
            turtle.forward(b) 


while(True):
    turtle.pencolor("purple")
    turtle.pensize(2)
    turtle.colormode(250)
    turtle.begin_fill()

    turtle.fillcolor(250,100,100)  

    daphne(190,100)

    turtle.end_fill()
    