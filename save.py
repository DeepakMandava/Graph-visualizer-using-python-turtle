from operations import operations
import datetime
from PIL import ImageGrab

class save(operations):
    def __init__(self,g,b,d):
        self.g=g
        self.b=b
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
        filepath = "image.jpg"
        ss = ImageGrab.grab()
        ss.save(filepath)

        f = open("Graph.txt",'w')
        f.write("Graph:\n")
        f.write("Node: connected nodes(with spaces)\n")
        for i in self.g:
            line = str(i)+" : "+" ".join(self.g[i])+"\n"
            f.write(line)
        line = "\nBFS starting with node-"+self.b[0]+": "
        f.write(line)
        for i in self.b:
            f.write(i+"  ")
        line = "\nDFS starting with node-"+self.b[0]+": "
        f.write(line)
        for i in self.d:
            f.write(i+"  ")
    
    def bfs():
        pass
    
    def dfs():
        pass
