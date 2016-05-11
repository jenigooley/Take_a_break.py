import turtle
def turtle_tank():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick() 
def draw_square():  
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("purple")
    brad.speed(3)
    count = 0
    while count <=  4:
        brad.forward(100)
        brad.right(90)
        count += 1
def draw_circle():        
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(2)
    angie.circle(100)
def draw_triangle():
    harps = turtle.Turtle()
    harps.shape("square")
    harps.color("yellow") 
    harps.speed(2)
    count = 0
    while count < 3:
        harps.backward(100)
        harps.left(120)
        count += 1
turtle_tank() 
