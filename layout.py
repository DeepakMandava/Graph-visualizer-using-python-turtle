'''
Title:      Graph visualiser with BFS(Breadth first search) and DFS(Depth first search)
Author:     Deepak Mandava
Created on: 30-01-2022
version:     version-1(protype)

'''
import turtle
from tkinter import messagebox

#x1,y1 are coordinates for labeling buttons
x1,y1=-501,286

# maximising turtle window
wn = turtle.Screen()
wn.setup(width=1.0,height=1.0)

#creating a pen to draw
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(10)

# creating buttons
class layout:
    def __init__(self,x1,x2,y1,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    # skeleton of buttons
    def drawbuttons(self):
        i=0
        while i<7:
            pen.penup()
            pen.goto(self.x1+i*150,self.y1)
            pen.pendown()
            pen.goto(self.x2+i*150,self.y1)
            pen.goto(self.x2+i*150,self.y2)
            pen.goto(self.x1+i*150,self.y2)
            pen.goto(self.x1+i*150,self.y1)
            i=i+1
    # specify area where to draw graph
    def grapharea(self):
        pen.penup()
        pen.goto(-610,240)
        pen.pendown()
        pen.goto(600,240)
        pen.write("(600,240)",align="center")
        pen.goto(600,-300)
        pen.write("(600,-300)",align="center")
        pen.goto(-610,-300)
        pen.write("(-600,-300)",align="center")
        pen.goto(-610,240)
        pen.write("(-610,240)",align="center")
        pen.penup()

def gui():          
    
    draw = layout(-571,-431,312,272)
    draw.drawbuttons()
    draw.grapharea()
    
    #Labelling buttons
    pen.goto(x1,y1)
    pen.write("Add Node",align="center")
    pen.goto(x1+150,y1)
    pen.write("delete Node",align="center")
    pen.goto(x1+300,y1)
    pen.write("Add Edge",align="center")
    pen.goto(x1+450,y1)
    pen.write("Delete Edge",align="center")
    pen.goto(x1+600,y1)
    pen.write("Save Graph",align="center")
    pen.goto(x1+750,y1)
    pen.write("BFS",align="center")
    pen.goto(x1+900,y1)
    pen.write("DFS",align="center")
    
    #About BFS and DFS
    pen.goto(-200,220)
    pen.write("Please click save button only after BFS and DFS are done.BFS and DFS will be written in saved file and also you will be getting an image showing graph",align="center",font=("Arial","12","normal"))
