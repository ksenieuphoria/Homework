import turtle

window = turtle.Screen()
window.bgcolor('silver')
window.setup(700, 700)
window.title("Turtle")

turtle.shape("turtle")

turtle.color('green')
turtle.down()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.up()
turtle.forward(150)

turtle.color('blue')
turtle.down()
turtle.forward(100)
turtle.left(90)
turtle.forward(270)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(270)
turtle.up()
turtle.forward(90)
turtle.exitonclick()