'''
Title:      Graph visualiser with BFS(Breadth first search) and DFS(Depth first search)
Author:     Deepak Mandava
Created on: 30-01-2022
version:     version-1(protype)

'''
from layout import *
from operations import operations

class dfs(operations):
    def __init__(self,g,c,d):
        self.g=g
        self.c=c
        self.d=d

    def addNode(self):
        pass

    def delNode(self):
        pass

    def addEdge(self):
        pass

    def delEdge(self):
        pass

    def save(self):
        pass

    def bfs(self):
        pass
    
    def dfs(self):
        pen.speed(1)   # speed is decreased inorder to slow the animation
        visited = []   #List for visited nodes.
        graph = self.g
        node = turtle.textinput("Starting node","Enter node from where you want to start DFS")
        def dfs_function(visited, graph, node):  #function for dfs 
                if node not in visited:
                    self.d.append(node)
                    xcor,ycor=self.c[node]
                    pen.goto(int(xcor),int(ycor))
                    pen.dot(30,"red")
                    pen.dot(30,"yellow")
                    pen.dot(20,"white")
                    pen.write(node,align="center")
                    visited.append(node)
                    for neighbour in self.g[node]:
                        dfs_function(visited,graph, neighbour)
        if node!='None' and node!='':
            dfs_function(visited,graph,node)
        elif node=='':
            messagebox.showwarning("warning","please enter lable of node from where you want to start BFS")
            self.bfs()
        self.g = graph
        pen.speed(10)
        print(self.b)