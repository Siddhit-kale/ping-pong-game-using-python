import turtle as t
import os

ball_speed = 1
paddle_speed = 30

player_a_score = 0
player_b_score = 0

win = t.Screen()
win.title("Ping-Pong Game")
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

paddle_left = t.Turtle()
paddle_left.speed(10)
paddle_left.shape('square')
paddle_left.color('red')
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

paddle_right = t.Turtle()
paddle_right.speed(10)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color('red')
paddle_right.penup()
paddle_right.goto(350, 0)

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)
ball_dx = ball_speed
ball_dy = ball_speed

pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0                    Player B: 0 ", align="center", font=('Monaco', 24, "normal"))

def game_over(winner):
    pen.clear()
    pen.write(f"Game Over! {winner} wins with a score of {player_a_score if winner == 'Player A' else player_b_score}",
              align="center", font=('Monaco', 24, "normal"))
    win.onkeypress(restart_game, "r")  # Bind "R" key to restart the game

def restart_game():
    global player_a_score, player_b_score, ball_dx, ball_dy
    player_a_score = 0
    player_b_score = 0
    pen.clear()
    pen.write("Player A: 0                    Player B: 0 ", align="center", font=('Monaco', 24, "normal"))
    ball.goto(0, 0)
    ball_dx = ball_speed
    ball_dy = ball_speed
    game_loop()
    
def paddle_left_up():
    y = paddle_left.ycor()
    y += paddle_speed
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= paddle_speed
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += paddle_speed
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= paddle_speed
    paddle_right.sety(y)

win.listen()
win.onkeypress(paddle_left_up, "w")
win.onkeypress(paddle_left_down, "s")
win.onkeypress(paddle_right_up, "Up")
win.onkeypress(paddle_right_down, "Down")

def game_loop():
    global player_a_score, player_b_score, ball_dx, ball_dy
    while True:
        win.update()
        ball.setx(ball.xcor() + ball_dx)
        ball.sety(ball.ycor() + ball_dy)

        if ball.ycor() > 290 or ball.ycor() < -290:
            ball_dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball_dx *= -1
            player_a_score += 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                      align="center", font=('Monaco', 24, "normal"))
            os.system("afplay wallhit.wav&")

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball_dx *= -1
            player_b_score += 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                      align="center", font=('Monaco', 24, "normal"))
            os.system("afplay wallhit.wav&")
            
        if ball.distance(paddle_right) < 50 and ball.xcor() > 340:
            ball.setx(340)
            ball_dx *= -1
            os.system("afplay paddle.wav&")

        if ball.distance(paddle_left) < 50 and ball.xcor() < -340:
            ball.setx(-340)
            ball_dx *= -1
            os.system("afplay paddle.wav&")

        if player_a_score >= 20:
            game_over("Player A")
            break
        elif player_b_score >= 20:
            game_over("Player B")
            break

win.setup(width=1000, height=600)

game_loop()
