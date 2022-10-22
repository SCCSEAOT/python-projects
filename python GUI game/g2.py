import turtle
import random
import winsound
import time
score=0

bg=turtle.Screen()
bg.setup(650,650)
bg.bgpic("we3.gif")
bg.bgcolor("black")
bg.title("FIRE")

#write score and intro..
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,0)
pen.write("WELCOME TO SPACE\nENEMIES ARE WAITING FOR YOU\nYOU ARE OUR ONLY HOPE\nSAVE OUR MOTHER EARTH",align="center",font=33)
time.sleep(4)
pen.clear()
pen.goto(0,280)

#seing gun
g=turtle.Turtle()
g.shape("triangle")
g.speed(0)
g.left(90)
g.color('red')
g.penup()
g.goto(0,-300)
g.speed(0)

#set bullet
b=turtle.Turtle()
b.shape("arrow")
b.speed(0)
b.left(90)
b.shapesize(0.1,1.4)
b.penup()
b.goto(0,-293)
b.speed(0)
b.color("#abcfff")

def fire():
    winsound.Beep(1050,100)
    while(b.ycor()<300):
        y=b.ycor()
        b.sety(y+15)
        b.speed(0)
def fireb():
    winsound.Beep(70,100)
    while(b1.ycor()>-300):
        y=b1.ycor()
        b1.sety(y-40)
        b1.speed(0)    
#move the gun
def right():
    g.setx(g.xcor()+10)
    b.setx(g.xcor())
    g.speed(0)
    b.speed(0)    
def left():
    g.setx(g.xcor()-10)
    b.setx(g.xcor())
    g.speed(0)
    b.speed(0)

#make aliens
a=turtle.Turtle()
a.shape("circle")
a.speed(0)
a.shapesize(2)
a.penup()
a.goto(0,293)
a.speed(0)
a.color("#abc000")
a.speed(0)
#make enemy bullet
b1=turtle.Turtle()
b1.shape("arrow")
b1.speed(0)
b1.left(90)
b1.shapesize(0.2,1.8)
b1.left(180)
b1.penup()
b1.goto(a.xcor(),a.ycor()-23)
b1.speed(0)
b1.color("#aaa33f")
#keyboard
bg.listen()
bg.onkeypress(fire,"f")
bg.onkeypress(left,"a")
bg.onkeypress(right,"d")

#move enemy
G=1.8
s=2.4
h=0
while True:
    bg.update()
    #print(g.xcor())
    a.setx(a.xcor()+s)
    a.sety(a.ycor()+G)
    q=random.randint(0,10)
    g.color("red")
    if(q==1):
        fireb()
        
    else:
        b1.goto(a.xcor(),a.ycor())
        #print(q)
    if(a.xcor()>300 or a.xcor()<-300):
        s*=-1
    if(b.distance(a)<54 or (a.xcor()==b.xcor() and a.ycor()==b.ycor())):
        a.color("red")
        winsound.PlaySound('Comet-SoundBible.com-1256431940.wav',winsound.SND_FILENAME)
        a.color("#abc000")
        a.goto(random.randint(0,295),random.randint(240,295))
        b.goto(g.xcor(),-293)
        score+=10
        pen.clear()
        pen.write("Score {}".format(score),align="center",font=33)
    if(a.ycor()>295 or a.ycor()<220):
        G*=-1
    if(b.ycor()>300):
        b.goto(g.xcor(),-293)

    if(b1.distance(g)<20):
        
        winsound.Beep(400,100)
        g.color("white")
        
        h+=1
    if(h>=5):
        p=turtle.Turtle()
        p.speed(0)
        p.color("red")
        p.penup()
        p.hideturtle()
        p.goto(0,0)
        p.write("GAME OVER",font=40)
        break

winsound.PlaySound('COFFIN.wav',winsound.SND_FILENAME)















