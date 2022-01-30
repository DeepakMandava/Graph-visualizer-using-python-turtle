from operations import operations
from layout import *
import re

class node(operations):
    def __init__(self,g,c):
        self.g=g
        self.c=c

    def addNode(self):
        n = turtle.textinput("Add Node","Enter label for node(A-z)")
        if re.compile("[A-z]").fullmatch(n) is not None:
            if n not in self.g:
                xcor = turtle.numinput("Node coordinates","Enter x-coordinate for node:",minval=-600,maxval=590)
                ycor = turtle.numinput("Node coordinates","Enter y-coordinate for node:",minval=-290,maxval=230)
                if xcor!='None' and ycor!='None':
                    self.g[n]=[]
                    self.c[n]=[xcor,ycor]
                    pen.goto(int(xcor),int(ycor))
                    pen.dot(30,"yellow")
                    pen.dot(20,"white")
                    pen.write(n,align="center")
                else:
                    messagebox.showwarning("warning","Adding node is terminated. Please try again")
            else:
                messagebox.showwarning("warning","Please dont give lables that already exist")
                self.addNode()
            
        elif n=='':
            messagebox.showwarning("warning","Please give lables for the node!!!!!")
            self.addNode()

    def delNode(self):
        n = turtle.textinput("Delete Node","Enter label of node which is to be deleted")
        if re.compile("[A-z]").fullmatch(n) is not None:
            if n in self.g and n in self.c:
                self.g.pop(n)
                xcor,ycor = self.c[n]
                pen.goto(int(xcor),int(ycor))
                pen.dot(50,"white")
                self.c.pop(n)
                messagebox.showwarning("warning","your requested node and its edges are removed from graph")
            else:
                messagebox.showwarning("warning","Please enter label of node thats present in graph")
                self.delNode()
        elif n=='':
            messagebox.showwarning("warning","Please enter lables of node!!!!!!")
            self.delNode()

    def addEdge(self):
        pass

    def delEdge(self):
        pass

    def save():
        pass

    def bfs():
        pass
    
    def dfs():
        pass
