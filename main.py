from layout import *
import node,edge,save,bfs,dfs

graph = dict() #To store graph
coor = dict()  #To store coordinates of nodes
bfs_l = []   #To store bfs
dfs_l = []   #To store dfs

def functioncall(x,y):
    obj_n = node.node(graph,coor)
    obj_e = edge.edge(graph,coor)
    obj_s = save.save(graph,bfs_l,dfs_l)
    obj_b = bfs.bfs(graph,coor,bfs_l)
    obj_d = dfs.dfs(graph,coor,dfs_l)
    
    pen.goto(x,y)#capturing mouse coordinates to validate them and call appropriate functions
    
    if -571<int(pen.xcor())<-431 and 272<int(pen.ycor())<312:
        obj_n.addNode()
        
    elif -571<int(pen.xcor()-150.0)<-431 and 272<int(pen.ycor())<312:
        obj_n.delNode()
        
    elif -571<int(pen.xcor()-300.0)<-431 and 272<int(pen.ycor())<312:
        obj_e.addEdge()
        
    elif -571<int(pen.xcor()-450.0)<-431 and 272<int(pen.ycor())<312:
        obj_e.delEdge()
        
    elif -571<int(pen.xcor()-600.0)<-431 and 272<int(pen.ycor())<312:
        obj_s.save()
    
    elif -571<int(pen.xcor()-750.0)<-431 and 272<int(pen.ycor())<312:
        obj_b.bfs()

    elif -571<int(pen.xcor()-900.0)<-431 and 272<int(pen.ycor())<312:
        obj_d.dfs()        

def main():
    #calling gui function to draw skeleton of interface
    gui()  
    # helps us to make buttons diagrams to work as actual buttons
    wn.onclick(functioncall)

main()
turtle.done()