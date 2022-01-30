from operations import operations
from layout import *

class edge(operations):
    def __init__(self,g,c):
        self.g=g
        self.c=c
    
    def addNode(self):
        pass
    
    def delNode(self):
        pass
    
    def addEdge(self):
        n1 = turtle.textinput("Add Edge","Enter label of node from which node is to drawn")
        n2 = turtle.textinput("Add Edge","Enter label of node to which node is to drawn")
        if n1!='None' and n2!='None':            
            xcor,ycor = self.c[n1]
            pen.penup()
            pen.goto(int(xcor),int(ycor))
            pen.pendown()
            xcor,ycor = self.c[n2]
            pen.goto(int(xcor),int(ycor))
            if n2 not in self.g[n1]:
                self.g[n1].append(n2)
            if n1 not in self.g[n2]:
                self.g[n2].append(n1)
        elif n1=='' or n2=='':
            messagebox.showwarning("warning","Please enter valid lable of node that present in graph")
            seld.addEdge()
        pen.penup()
    
    def delEdge(self):
        pen.color("white")
        n1 = turtle.textinput("Delete Edge","Enter label of node from which node is to deleted")
        n2 = turtle.textinput("Delete Edge","Enter label of node to which node is to deleted")
        if n1!='None' and n2!='None':
            xcor,ycor = self.c[n1]
            pen.goto(int(xcor),int(ycor))
            pen.pendown()
            xcor,ycor = self.c[n2]
            pen.goto(int(xcor),int(ycor))
            pen.color("black")
            if n2 in self.g[n1]:
                self.g[n1].remove(n2)
            if n1 in self.g[n2]:
                self.g[n2].remove(n1)
        elif n1=='' or n2=='':
            messagebox.showwarning("warning","Please enter valid lable of node that present in graph")
            self.delEdge()
        pen.penup()

    def save():
        pass
    
    def bfs():
        pass

    def dfs():
        pass