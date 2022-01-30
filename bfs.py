from layout import *
from operations import operations

class bfs(operations):
    def __init__(self,g,c,b):
        self.g=g
        self.c=c
        self.b=b

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
        pen.speed(1)   # speed is decreased inorder to slow the animation
        visited = []   #List for visited nodes.
        queue = []     #Initialize a queue
        node = turtle.textinput("Starting node","Enter node from where you want to start BFS")
        if node!='None' and node!='':
            visited.append(node)
            queue.append(node)
            while queue:          # Creating loop to visit each node
                m = queue.pop(0)
                xcor,ycor=self.c[m]
                pen.goto(int(xcor),int(ycor))
                pen.dot(30,"red")
                pen.dot(30,"yellow")
                pen.dot(20,"white")
                pen.write(m,align="center")
                self.b.append(m)
                for neighbour in self.g[m]:
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.append(neighbour)
        elif node=='':
            messagebox.showwarning("warning","please enter lable of node from where you want to start BFS")
            self.bfs()
        pen.speed(10)

    def dfs():
        pass