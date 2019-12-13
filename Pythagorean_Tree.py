import turtle  
import math  


def pyth_tree(jim, depth, maxdepth):
    if depth > maxdepth:
        return
    length = 180*((math.sqrt(2)/2)**depth)
    bill = jim.clone()
    jim.forward(length)
    jim.left(45)
    pyth_tree(jim, depth+1, maxdepth)
    bill.right(90)
    bill.forward(length)
    bill.left(90)
    bill.forward(length)
    if depth != maxdepth:
        turt3 = bill.clone()
        turt3.left(45)
        turt3.forward(180*((math.sqrt(2)/2)**(1+depth)))
        turt3.right(90)
        pyth_tree(turt3, depth+1, maxdepth)
    bill.left(90)
    bill.forward(length)  
n=int(input('Dimension:'))

def draw_tree(n):
    window = turtle.Screen()
    turt = turtle.Turtle()
    
    turt.penup()
    turt.goto(-75, -225)
    turt.pendown()
    turt.speed(1)
    turt.left(90)
    pyth_tree(turt, 1, n)
    window.exitonclick()  


draw_tree(n)  
