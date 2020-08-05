import turtle
import random
import time
import winsound #Sound

#HIGH SCORE
with open("highscore.txt","r") as f:
    highscore=f.read()  #value will be stored as a string
    

player_sc=0
player_live=5
a=0
b=0
high_sc=int(highscore)

is_right=True
is_right1=True
is_left=True
is_left1=True

level=1
max_speed=2
special_list=[10,27,60,90]
level_list=[30,60] # denotes level 2 and 3
corona_list=[70,72,73,74,80,81,82,85,86]
pc=turtle.Screen()
pc.title("Falling Skies")
pc.setup(width=800, height=600)
#pc.bgcolor('black')
pc.bgpic("images/fallingskiesbg.gif")
pc.tracer(0,0)


#level1 name
wrlevel=turtle.Turtle()
wrlevel.speed(0)  
wrlevel.color("blue")
wrlevel.shape("turtle")
wrlevel.penup()
wrlevel.hideturtle()
wrlevel.goto(0,0)


wrlevel.write("WELCOME TO",align="center",font=("decorative",40,"bold"))
wrlevel.goto(0,-50)
wrlevel.write("Falling Skies",align="center",font=("formal",40,"bold"))
time.sleep(4)
wrlevel.clear()
wrlevel.goto(0,50)
wrlevel.write("Rules",align="center",font=("decorative",40,"bold"))
wrlevel.goto(0,0)
wrlevel.write("1.Initially the player has 5 lives.",align="center",font=("formal",14,"bold"))
wrlevel.goto(0,-50)
wrlevel.write("2.Player Has to collect Fruits to increase the score and the score increases by 1. ",align="center",font=("formal",14,"bold"))
wrlevel.goto(0,-100)
wrlevel.write("3.When the bullet hits the player , the lives decreases. ",align="center",font=("formal",14,"bold"))
wrlevel.goto(0,-150)
wrlevel.write("Note:Press P key to pause the game.",align="center",font=("formal",14,"bold"))
time.sleep(15)
wrlevel.clear()



#Change Background Pic for sometime

pc.bgpic('images/control.gif')
# time.sleep(15)

# Register Images

pc.register_shape("images/camel1.gif")
pc.register_shape("images/camel3.gif")
pc.register_shape("images/ammo.gif")
pc.register_shape("images/bullet.gif")
pc.register_shape("images/mango.gif")
pc.register_shape("images/pineapple.gif")
pc.register_shape("images/apple.gif")
pc.register_shape("images/pear.gif")
pc.register_shape("images/virus.gif")
pc.register_shape("images/dir_right.gif")
pc.register_shape("images/dir_left.gif")

# Player 
player=turtle.Turtle()
player.speed(0)
player.shape("images/camel1.gif")
player.color("red")
player.penup()
player.goto(0,-250)
player.direction="stop"


#create a list of Bullets and Fruits
bullets=[]
for _ in range(10):
    bullet=turtle.Turtle()
    bullet.speed(0)
    bullet.shape("images/ammo.gif")
    bullet.color("yellow")
    bullet.penup()
    x=random.randint(-350,350)
    y=random.randint(330,1000)
    bullet.goto(x,y)
    bullet.speed=random.randint(0,1)
    bullets.append(bullet)

# Pineapple is a special fruit
pineapple=turtle.Turtle()
pineapple.speed(0)
pineapple.shape("images/pineapple.gif")
pineapple.color("yellow")
pineapple.penup()
x=random.randint(-350,350)
y=random.randint(340,1000)
pineapple.goto(x,y)
pineapple.speed=random.randint(0,1)


apple_right=turtle.Turtle()
apple_right.speed(6)
apple_right.shape("images/apple.gif")
apple_right.color("yellow")
apple_right.penup()
apple_right.goto(360,340)

dir_right=turtle.Turtle()
dir_right.speed(0)
dir_right.shape("images/dir_right.gif")
dir_right.color("yellow")
dir_right.penup()
dir_right.goto(360,500)
dir_right.speed=random.randint(0,1)

dir_left=turtle.Turtle()
dir_left.speed(0)
dir_left.shape("images/dir_left.gif")
dir_left.color("yellow")
dir_left.penup()
dir_left.goto(360,500)
dir_left.speed=random.randint(0,1)


food_mangoes=[]
for _ in range(20):
    food_mango=turtle.Turtle()
    food_mango.speed(0)
    food_mango.shape("images/mango.gif")
    food_mango.color("yellow")
    food_mango.penup()
    x=random.randint(-350,350)
    y=random.randint(330,1000)
    food_mango.goto(x,y)
    food_mango.speed=random.randint(0,1)
    food_mangoes.append(food_mango)


corona=turtle.Turtle()
corona.speed(1)
corona.shape("images/virus.gif")
corona.penup()
x=random.randint(-350,350)
y=random.randint(350,1000)
corona.goto(x,y)

#writing
wr=turtle.Turtle()
wr.speed(0)  
wr.color("yellow")
wr.shape("turtle")
wr.penup()
wr.hideturtle()
wr.goto(0,270)
wr.write("SCORE: {}  LIVES: {}".format(player_sc,player_live),align="center",font=("arial",20,"normal"))

# Player's Direction

def player_left():
    global is_left
    player.direction="left"
    player.shape("images/camel1.gif")
    is_left=False
    #x=player.xcor()
    #x-=7
    #player.setx(x)

def player_right():
    global is_right
    player.direction="right"
    player.shape("images/camel3.gif")
    is_right=False
    #x=player.xcor()
    #x+=7
    #player.setx(x)

def player_stop():
    player.direction="stop"


# Pause Funtionality
is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused=False
    else:
        is_paused=True    

# Onkey Press Events
pc.listen()
pc.onkeypress(player_left,"Left")
pc.onkeypress(player_right,"Right")
pc.onkeypress(player_stop,"space")
pc.onkeypress(toggle_pause,"p")

# Write Again
time.sleep(15)
pc.bgpic("images/fallingskiesbg.gif")

wr2=turtle.Turtle()
wr2.speed(0)  
wr2.color("blue")
wr2.shape("turtle")
wr2.penup()
wr2.hideturtle()
wr2.goto(0,0)
wr2.write("TUTORIAL",align="center",font=("arial",20,"bold"))


#Tutorials 
while is_right:
    if is_right1 is True:
        pc.update()
        y=apple_right.ycor()
        y-=0.5
        apple_right.sety(y)
        if(apple_right.ycor()<=200):
            is_right1=False
    else:
        pc.update()
        dir_right.goto(player.xcor()+60,player.ycor())
        wrlevel.goto(0,-50)
        wrlevel.write("PRESS RIGHT KEY",align="center",font=("formal",40,"bold"))


dir_right.goto(450,500)
wrlevel.clear()
is_right=True
while is_right:
    y=apple_right.ycor()
    y-=0.5
    apple_right.sety(y)
    
    if(player.xcor()>360):
        player.setx(360)
    elif(player.xcor()<-360):
        player.setx(-360)
        
    if(player.direction=="left"):
        x=player.xcor()
        x-=1
        player.setx(x)
    elif(player.direction=="right"):
        x=player.xcor()
        x+=1
        player.setx(x)
    if(player.distance(apple_right)<40):
        apple_right.goto(-360,340)
        is_right=False
    pc.update()


while is_left:
    if is_left1 is True:
        pc.update()
        y=apple_right.ycor()
        y-=0.5
        apple_right.sety(y)
        if(apple_right.ycor()<=200):
            is_left1=False
    else:
        pc.update()
        dir_left.goto(player.xcor()-100,player.ycor())
        wrlevel.goto(0,-50)
        wrlevel.write("PRESS LEFT KEY",align="center",font=("formal",40,"bold"))


dir_left.goto(450,500)
wrlevel.clear()
is_left=True
while is_left:
    y=apple_right.ycor()
    y-=0.5
    apple_right.sety(y)
    
    if(player.xcor()>360):
        player.setx(360)
    elif(player.xcor()<-360):
        player.setx(-360)
        
    if(player.direction=="left"):
        x=player.xcor()
        x-=1
        player.setx(x)
    elif(player.direction=="right"):
        x=player.xcor()
        x+=1
        player.setx(x)
    if(player.distance(apple_right)<40):
        apple_right.goto(500,500)
        is_left=False
    pc.update()


        
wr2.clear()
wrlevel.goto(0,0)
wrlevel.write("LEVEL: {}".format(level),align="center",font=("formal",20,"bold"))
winsound.PlaySound("audio/level-complete.wav",winsound.SND_ASYNC)
time.sleep(2)
# Tutorial Ends Above

# Game Levels
def game_level(level):
    if(level==2):
        for i in food_mangoes:
            i.shape("images/apple.gif")
        for i in bullets:
            i.shape("images/bullet.gif")
        pc.bgpic("images/fallingskiesbg1.gif")
    elif(level==3):
        for i in food_mangoes:
            i.shape("images/pear.gif")
        for i in bullets:
            i.shape("images/virus.gif")
        pc.bgpic("images/fallingskiesbg2.gif")


# Main Game Loop

while True:
    if not is_paused:

        pc.update()

        wrlevel.clear()
        #Reassigning Position if the object crossed the boundary
        if(player.xcor()>360):
            player.setx(360)
        elif(player.xcor()<-360):
            player.setx(-360)
        
        if(player.direction=="left"):
            x=player.xcor()
            x-=2.5
            player.setx(x)
        elif(player.direction=="right"):
            x=player.xcor()
            x+=2.5
            player.setx(x)

        if(level!=3):
            for i in bullets:
                y=i.ycor()
                y-=random.randint(1,max_speed)
                i.sety(y)
            
        else:
            for i in bullets:
                y=i.ycor()
                y-=random.randint(1,max_speed)
                i.sety(y)
                if(y<=random.randint(-50,50)):# Adding deviation to the Path in level 3
                    x=i.xcor()
                    x=random.randint(x-5,x+5)   
                    i.setx(x) 

             
        # Checking Player and Bullets Collision
        for i in bullets:
            if(i.distance(player)<40):
                i.sety(random.randint(200,1000))
                i.setx(random.randint(-350,350))
                player_live-=1
                winsound.PlaySound("audio/hurt.wav",winsound.SND_ASYNC)
                wr.clear()
                if player_sc>int(highscore):
                    highscore=player_sc
                    # print(highscore)
                wr.write("SCORE: {}  LIVES: {}  HIGH SCORE: {}".format(player_sc,player_live,highscore),align="center",font=("arial",20,"normal"))
                
                
        #Reassigning Position if the object crossed the boundary
        for i in bullets:
            if(i.ycor()<-300):
                i.sety(random.randint(200,1000))
                i.setx(random.randint(-350,350))

        if(level!=3):
            for i in food_mangoes:
                y=i.ycor()
                y-=random.randint(1,max_speed)
                i.sety(y)
            
        else:    
            for i in food_mangoes:
                y=i.ycor()
                y-=random.randint(1,max_speed)
                i.sety(y)
                if (y<= random.randint(-50,50)):# Adding deviation to the Path in level 3
                    x=i.xcor()
                    x=random.randint(x-5,x+5)   
                    i.setx(x)

        #Checking Player and Fruits(Mango) Collision
        for i in food_mangoes:
            if(i.distance(player)<40):
                i.sety(random.randint(200,1000))
                i.setx(random.randint(-350,350))
                player_sc+=1
                winsound.PlaySound("audio/2_bounce.wav",winsound.SND_ASYNC)
                wr.clear()
                if player_sc>int(highscore):
                    highscore=player_sc
                    # print(highscore)
                wr.write("SCORE: {}  LIVES: {}  HIGH SCORE: {}".format(player_sc,player_live,highscore),align="center",font=("arial",20,"normal"))
                
        #Reassigning Position if the object crossed the boundary
        for i in food_mangoes:
            if(i.ycor()<-300):
                i.sety(random.randint(200,1000))
                i.setx(random.randint(-350,350))

        if player_sc in special_list:
            a=1
        
        if(a==1):
            y=pineapple.ycor()
            y-=random.randint(2,3)
            pineapple.sety(y)

        #Checking Player and Fruits(Pineapple) Collision
        if(pineapple.distance(player)<40):
            pineapple.sety(random.randint(340,400))
            pineapple.setx(random.randint(-350,350))
            a=0
            player_sc+=10
            winsound.PlaySound("audio/powerup.wav",winsound.SND_ASYNC)
            wr.clear()
            if player_sc>int(highscore):
                    highscore=player_sc
                    # print(highscore)
            wr.write("SCORE: {}  LIVES: {}  HIGH SCORE: {}".format(player_sc,player_live,highscore),align="center",font=("arial",20,"normal"))
                
        #Reassigning Position if the object crossed the boundary 
        if(pineapple.ycor()<-300):
            pineapple.sety(random.randint(340,400))
            pineapple.setx(random.randint(-350,350))
            a=0

        if player_sc in corona_list:
            b=1
        
        if(b==1):
            y=corona.ycor()
            y-=random.randint(2,3)
            corona.sety(y)

        #Checking Player and Corona Collision 
        if(corona.distance(player)<40):
            corona.sety(random.randint(340,400))
            corona.setx(random.randint(-350,350))
            b=0
            player_live-=2
            winsound.PlaySound("audio/powerup.wav",winsound.SND_ASYNC)
            wr.clear()
            wr.write("SCORE: {}  LIVES: {}".format(player_sc,player_live),align="center",font=("arial",20,"normal"))
        #Reassigning Position if the object crossed the boundary  
        if(corona.ycor()<-300):
            corona.sety(random.randint(340,400))
            corona.setx(random.randint(-350,350))
            b=0

        #Increasing Game Level
        if player_sc in level_list:
            level+=1
            winsound.PlaySound("audio/level-complete.wav",winsound.SND_ASYNC)
            game_level(level)
            wrlevel.write("LEVEL: {}".format(level),align="center",font=("normal",20,"bold"))
            time.sleep(2)
            wrlevel.clear()
            player_sc+=1
            max_speed+=1
            player_live+=1
            

        # Game Over 
        if(player_live<=0):
            wr1=turtle.Turtle()
            wr1.speed(0)  
            wr1.color("blue")
            wr1.shape("turtle")
            wr1.penup()
            wr1.hideturtle()
            wr1.goto(0,0)
            wr1.write("GAME OVER",align="center",font=("arial",60,"normal"))
            winsound.PlaySound("audio/gameover.wav",winsound.SND_ASYNC)
            with open("highscore.txt","w") as f:
                f.write(str(highscore))  #value will be stored as a string
            if(player_sc>high_sc):
                time.sleep(3)
                wr1.clear()
                wr1.color("white")
                wr1.write("Congratulation!",align="center",font=("arial",40,"normal"))
                winsound.PlaySound("audio/applause.wav",winsound.SND_ASYNC)
                wr1.goto(0,-60)
                wr1.write("New High Score",align="center",font=("arial",40,"normal"))
                
            break
    else:
        pc.update()
        wrlevel.write("Press P again to Resume",align="center",font=("arial",40,"normal"))
                    

turtle.done()