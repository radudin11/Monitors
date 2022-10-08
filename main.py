# Monitors problem:
# input = adjacency matrix of an undirected graph
# output = minium number of nodes so that all edges are covered
# by at least one node


# proposed method in README.md
from queue import PriorityQueue
import argparse

def readGraph(inputFile):
    dim = [int(x) for x in next(inputFile).split()][0]
    return [dim, [[int(x) for x in line.split()] for line in inputFile]]

def createPriorityQueue(graph, dim):
    q = PriorityQueue(dim)
    for i in range(dim):
        vertexDegree = sum(graph[i])
        if vertexDegree > 0:
            # we add the vertex to the queue and set its priority to its degree
            q.put((vertexDegree, i))
    return q

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--inputFile",type=argparse.FileType('r') ,help="Input file")
    return parser.parse_args()

def main():
    args = parseArgs()
    if args.inputFile:
        dim, graph = readGraph(args.inputFile)
    else:    
        filePath = input("Enter the path of the input file: ")
        dim, graph = readGraph(open(filePath))
    
    stop = False
    nrOfVertices = 0
    while not stop:
        # create priority queue
        q = createPriorityQueue(graph, dim)
        if q.empty():
            stop = True
        else:
            # take the vertex with the lowest degree
            vertexDegree, vertex = q.get()
            # final solution will need to have all these vertices guaranteed
            nrOfVertices += vertexDegree
            # we remove the adjacent vertices and all their edges
            adjacenctVertices = [i for i in range(dim) if graph[vertex][i] == 1]
            for i in adjacenctVertices:
                for j in range(dim):
                    graph[i][j] = 0
                    graph[j][i] = 0
            
            print('\n') 
    print(nrOfVertices)
if __name__ == '__main__':
    main()