import turtle

# Variables
padMove = 40
backgroundColor = "black"
scWidth = 800
scHeight = 600
aPadColor = "white"
bPadColor = "white"
ballColor = "white"
textColor = "white"


# First Settings
wn = turtle.Screen()
wn.title("Pong by @BuyuluMahmut")
wn.bgcolor(backgroundColor)
wn.setup(width=scWidth, height=scHeight)
wn.tracer(0)



# Ball Coordinates
x_cor = 0
y_cor = 0

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color(aPadColor)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color(bPadColor)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color(ballColor)
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color(textColor)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
#pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Coordinates
corpen = turtle.Turtle()
corpen.speed()
corpen.color(textColor)
corpen.penup()
corpen.hideturtle()
corpen.goto(0,-260)

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += padMove
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= padMove
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += padMove
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= padMove
    paddle_b.sety(y)

def gameReset():
    ball.goto(0,0)
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)
    pen.clear()
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(gameReset, "r")

# Main game loop
while True:
    wn.update()
    print("Ball X Cor: " + str(ball.xcor()))
    print("Ball Y Cor: " + str(ball.ycor()))

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
    

    # # Paddle border control
    # if paddle_a.xcor() > 390:
    #     paddle_a.setx(390)

    # if paddle_a.xcor() < -390:
    #     paddle_a.setx(-390)

    # if paddle_b.xcor() > 390:
    #     paddle_b.setx(390)

    # if paddle_b.xcor() < -390:
    #     paddle_b.setx(-390)




    corpen.clear()
    corpen.write("X: {}  Y: {}".format(round(ball.xcor()), round(ball.ycor())), align="center", font=("Courier", 18, "normal"))
    
    