# Pong in Python
# Take 1 by Said


import turtle

wn = turtle.Screen()
wn.title("Pong by Said")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-375, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(375, 0)

# Ball

ball = turtle.Turtle()
ball.speed(-10)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

#Pen
pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 20, "bold"))


#Function

def paddle_a_up():
  y=paddle_a.ycor()
  y +=20
  paddle_a.sety(y)

def paddle_a_down():
  y=paddle_a.ycor()
  y -=20
  paddle_a.sety(y)

def paddle_b_up():
  y=paddle_b.ycor()
  y +=20
  paddle_b.sety(y)

def paddle_b_down():
  y=paddle_b.ycor()
  y -=20
  paddle_b.sety(y)

#Keyboard Binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down,"Down")

#Main Game Loop
while True:
  wn.update()

  #Move the ball
  ball.setx(ball.xcor()+ball.dx)
  ball.sety(ball.ycor()+ball.dy)

  #Borders
  if ball.ycor() > 280:
    ball.sety(280)
    ball.dy *= -1

  if ball.ycor() < -280:
    ball.sety(-280)
    ball.dy *= -1

  if ball.xcor() > 395:
    ball.goto(0, 0)
    ball.dx *= -1
    score_a += 1
    pen.clear()
    pen.write("Player A: {} Player B: {}". format(score_a, score_b), align="center", font=("Courier", 20, "bold"))


  if ball.xcor() < -395:
    ball.goto(0, 0)
    ball.dx *= -1
    score_b += 1
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))

  #Paddle and Ball Collisions
  if (ball.xcor)() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
    ball.setx(340)
    ball.dx *= -1

  if (ball.xcor)() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
    ball.setx(-340)
    ball.dx *= -1


