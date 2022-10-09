# does not work in all cases!!!!!


# Monitors problem:
# input = adjacency matrix of an undirected graph
# output = minium number of nodes so that all edges are covered
# by at least one node


# proposed method in README.md
from queue import PriorityQueue
import argparse
import copy

class GraphMatrix:
    def __init__(self, dim):
        self.dim = dim
        self.graph = [[0 for x in range(dim)] for y in range(dim)]
    
    def getDim(self):
        return self.dim
    
    def addEdge(self, i, j):
        self.graph[i][j] = 1
        self.graph[j][i] = 1
    
    def getGraph(self):
        return self.graph
    
    def getVertexDegree(self, vertex):
        return sum(self.graph[vertex])
    
    def getAdjacentVertices(self, vertex):
        return [i for i, x in enumerate(self.graph[vertex]) if x == 1]
    
    
    def removeVertex(self, vertex):
        for i in range(self.dim):
            self.graph[vertex][i] = 0
            self.graph[i][vertex] = 0

class GraphList:
    def __init__(self, dim):
        self.dim = dim
        self.graph = [[] for x in range(dim)]
    
    def getDim(self):
        return self.dim

    def addEdge(self, i, j):
        if j not in self.graph[i]:
            self.graph[i].append(j)
            self.graph[j].append(i)
    
    def getGraph(self):
        return self.graph

    def getVertexDegree(self, vertex):
        return len(self.graph[vertex])
    
    def getAdjacentVertices(self, vertex):
        return self.graph[vertex]

    def removeVertex(self, vertex):
        for i in self.graph[vertex]:
            self.graph[i].remove(vertex)
        self.graph[vertex] = []

def readGraph(inputFile):
    dim = [int(x) for x in next(inputFile).split()][0]
    ret = [dim, [[int(x) for x in line.split()] for line in inputFile]]
    inputFile.close()
    return ret


def createPriorityQueue(graph):
    q = PriorityQueue(graph.getDim())
    for i in range(graph.getDim()):
        vertexDegree = graph.getVertexDegree(i)
        if vertexDegree > 0:
            # we add the vertex to the queue and set its priority to its degree
            q.put((vertexDegree, i))
    return q

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--inputFile",type=argparse.FileType('r') ,help="Input file")
    parser.add_argument("-m","--matrix",action="store_true",help="Use matrix representation, default")
    parser.add_argument("-l","--list",action="store_true",help="Use list representation")
    return parser.parse_args()

def createGraph(args, dim, graph):
    if args.list:
        g = GraphList(dim)
    else:
        g = GraphMatrix(dim)

    # g = GraphList(dim)
    
    for i in range(dim):
        for j in range(dim):
            if graph[i][j] == 1:
                g.addEdge(i, j)
    return g

def getMinCover(g):
    nrOfVertices = 0
    stop = False

    while not stop:
        # create priority queue
        q = createPriorityQueue(g)
        if q.empty():
            stop = True
        else:
            # take the vertex with the lowest degree
            vertexDegree, vertex = q.get()
            # final solution will need to have all these vertices guaranteed
            nrOfVertices += vertexDegree
            # we remove the adjacent vertices and all their edges
            adjacenctVertices = copy.copy(g.getAdjacentVertices(vertex))
            for v in adjacenctVertices:
                g.removeVertex(v)
    return nrOfVertices

def main():
    args = parseArgs()
    if args.inputFile:
        dim, graph = readGraph(args.inputFile)
    else:    
        filePath = input("Enter the path of the input file: ")
        dim, graph = readGraph(open(filePath))
    

    g = createGraph(args, dim, graph)

    nrOfVertices = getMinCover(g)
     
    print(nrOfVertices)
if __name__ == '__main__':
    main()