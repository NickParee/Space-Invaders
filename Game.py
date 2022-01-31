import math
import turtle
import os
import random

#Set up the screen
mainScreen = turtle.Screen()
mainScreen.bgcolor("black")
mainScreen.title("Space Invaders")

#Draw border
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

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerSpeed = 15

#Choose a number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemySpeed = 2

#Create the players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletState = "ready"

#Move the player left and right
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
    #Declare bulletState as a global 
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        #Move the bullet to just above the player
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

#Create keyboard bindings
turtle.listen()
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")
turtle.onkey(fireBullet, "space")

#Main game loop
while True:

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40
            enemySpeed *= -1
            enemy.sety(y)
            
        if enemy.xcor() < -280:
            enemy.ycor()
            y -= 40
            enemySpeed *= -1
            enemy.sety(y)
        
        #Check for a collision between the bullet and the enemy
        if isCollison(bullet, enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletState = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        if isCollison(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over!")
            break


    #Move the bullet
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

    #Check to see if the bullet had gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"




delay = input("Enter to finish")




