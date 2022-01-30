import abc
# This is a container which holds all the operations that can be done on graph
class operations(abc.ABC):
    @abc.abstractclassmethod
    def addNode():
        pass
    @abc.abstractclassmethod
    def delNode():
        pass
    @abc.abstractclassmethod
    def addEdge():
        pass
    @abc.abstractclassmethod
    def delEdge():
        pass
    @abc.abstractclassmethod
    def save():
        pass
    @abc.abstractclassmethod
    def bfs():
        pass
    @abc.abstractclassmethod
    def dfs():
        pass