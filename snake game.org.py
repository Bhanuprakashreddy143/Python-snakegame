# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 11:40:03 2023

@author: S BHANUPRAKASH REDDY
"""

from tkinter import *
import tkinter
from tkinter.ttk import *
import time
win= Tk()
win.title("THE BOYS ( snake game )")
win.geometry("620x400")
win.configure(bg="black")

lb=Label(win,width=100,text="SNAKE GAME ",font=("Verdana",50),background="black",foreground="green")
lb.pack(padx=70)


def start():
   task=5
   x=0
   while(x<task):
      time.sleep(1)
      bar['value']+=20
      x+=1
      win.update_idletasks()
   Button(win,text="START GAME",command=game).pack(pady=10)
bar= Progressbar(win, orient=HORIZONTAL, length=500)
bar.pack(pady=40)
def game():
    #imports
    import turtle
    import time
    import random
    win.destroy()

    delay = 0.1

    #scores
    score = 0
    high_score = 0

    #set up screen
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor('black')
    wn.setup(width=600, height=634 )
    wn.tracer(0)

    #set up subscreen
    sb=turtle.Turtle()
    sb.penup()
    sb.goto(-300,325)
    sb.color("white")
    sb.begin_fill()
    for i in range(2):
        sb.fd(600)
        sb.rt(90)
        sb.fd(34)
        sb.rt(90)
    sb.end_fill()

    #snake head
    head = turtle.Turtle()
    head.speed(1)
    head.shape("square")
    head.color("gold")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

    #snake food
    food= turtle.Turtle()
    food.speed(0)
    food.shape("turtle")
    food.color("red")
    food.penup()
    food.goto(0,100)

    segments = []

    #scoreboards
    sc = turtle.Turtle()
    sc.speed(0)
    sc.shape("square")
    sc.color("#10094f")
    sc.penup()
    sc.hideturtle()
    sc.goto(0,290)
    sc.write("score: 0  High score: 0", align = "center", font=("ds-digital", 18, "normal"))

    #Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"
    def go_down():
        if head.direction != "up":
            head.direction = "down"
    def go_left():
        if head.direction != "right":
            head.direction = "left"
    def go_right():
        if head.direction != "left":
            head.direction = "right"
    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y+20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y-20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x-20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x+20)

    #keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")


    #MainLoop
    while True:
        wn.update()

        #check collision with border area
        if head.xcor()>279 or head.xcor()<-280 or head.ycor()>260 or head.ycor()<-286:
        
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide the segments of body
            for segment in segments:
                segment.goto(1000,1000) #out of range
            #clear the segments
            segments.clear()

            #reset score
            score = 0

            #reset delay
            delay = 0.1

            sc.clear()
            sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 18, "normal"))

        #check collision with food
        if head.distance(food) <20:
            # move the food to random place
            x = random.randint(-280,280)
            y = random.randint(-280,280)
            food.goto(x,y)

            #add a new segment to the head
            new_segment = turtle.Turtle()
            new_segment.speed(1)
            new_segment.shape("square")
            new_segment.color("gold")
            new_segment.penup()
            segments.append(new_segment)

            #shorten the delay
            delay -= 0.001
            #increase the score
            score += 10

            if score > high_score:
                high_score = score
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 18, "normal")) 

        #move the segments in reverse order
        for index in range(len(segments)-1,0,-1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x,y)
        #move segment 0 to head
        if len(segments)>0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()

        #check for collision with body
        for segment in segments:
            if segment.distance(head)<20:
                
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                #hide segments
                for segment in segments:
                    segment.goto(1000,1000)
                segments.clear()
                score = 0
                delay = 0.1

                #update the score     
                sc.clear()
                sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 18, "normal"))
        time.sleep(delay)
    

        
Button(win, text="click to load",command=start).pack(pady=5)
win.mainloop()