import math
import turtle
import os
import random

# Set up the screen
mainScreen = turtle.Screen()
mainScreen.bgcolor("black")
mainScreen.title("Space Invaders")
mainScreen.bgpic("space_invaders_background.gif")
mainScreen.tracer(0)

# Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set score to 0
score = 0

# Draw the score
scorePen = turtle.Turtle()
scorePen.speed(0)
scorePen.color("white")
scorePen.penup()
scorePen.setposition(-290, 280)
scoreString = "Score: {}" .format(score)
scorePen.write(scoreString, False, align="left", font=("Arial", 12, "normal"))
scorePen.hideturtle()


# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerSpeed = 15

# Choose a number of enemies
number_of_enemies = 15
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemyNumber = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemyNumber)
    y = enemy_start_y
    enemy.setposition(x, y)
    # Update the enemy number
    enemyNumber += 1
    if enemyNumber == 10:
        enemy_start_y -= 50
        enemyNumber = 0

enemySpeed = 0.05

# Create the players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 0.8

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletState = "ready"

# Move the player left and right
def moveLeft():
    x = player.xcor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)

def moveRight():
    x = player.xcor()
    x += playerSpeed
    if x > 280:
        x = 280
    player.setx(x)

def fireBullet():
    # Declare bulletState as a global 
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollison(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

# Create keyboard bindings
mainScreen.listen()
mainScreen.onkeypress(moveLeft, "Left")
mainScreen.onkeypress(moveRight, "Right")
mainScreen.onkeypress(fireBullet, "space")

# Main game loop
while True:
    
    mainScreen.update()

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemySpeed *= -1
            
        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemySpeed *= -1
        
        # Check for a collision between the bullet and the enemy
        if isCollison(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletState = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            enemy.setposition(0, 10000)
            # Update the score
            score += 10
            scoreString = "Score: {}" .format(score)
            scorePen.clear()
            scorePen.write(scoreString, False, align="left", font=("Arial", 12, "normal"))


        if isCollison(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over!")
            break


    # Move the bullet
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

    #  Check to see if the bullet had gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"




