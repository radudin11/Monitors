# repo: https://github.com/radudin11/Monitors


# Monitors problem:
# input = adjacency matrix of an undirected graph
# output = minium number of nodes so that all edges are covered
# by at least one node


# proposed method in README.md
from io import BufferedReader
from pickle import GLOBAL
from queue import PriorityQueue
import argparse
import copy
import sys
from tabnanny import check
import time

DEBUG = False


class Graph:
    def __init__(self, dim):
        self.dim = dim

    def getDim(self):
        return self.dim

    def addEdge(self, x, y):
        pass

    def removeVertex(self, x):
        pass

    def getAdjacentVertices(self, x):
        pass

    def getVertexDegree(self, x):
        pass

    def isCovered(self, guess: int) -> bool:
        combinations = getCombinations(guess, self.getDim())

        # check if any of the combinations is a cover
        for c in combinations:
            if self.isCover(c):
                if DEBUG:
                    print("Found cover: ", c)
                    print(guess)
                    print("")
                return True
        return False
    def isCover(self, Vertices: list) -> bool:
        # check if the graph is covered by Vertices

        gCopy = copy.deepcopy(self)

        for v in Vertices:
            gCopy.removeVertex(v)

        for i in range(gCopy.getDim()):
            if gCopy.getVertexDegree(i) > 0:
                return False
        return True

class GraphMatrix(Graph):
    def __init__(self, dim: int):
        self.dim = dim
        self.graph = [[0 for x in range(dim)] for y in range(dim)]

    def getDim(self) -> int:
        return self.dim

    def addEdge(self, i: int, j: int):
        if i >= self.dim or j >= self.dim:
            print("Error: vertex out of range")
            return

        self.graph[i][j] = 1
        self.graph[j][i] = 1

    def getGraph(self) -> list:
        return self.graph

    def getVertexDegree(self, vertex: int) -> int:
        if vertex >= self.dim:
            print("Error: vertex out of range")
            return 0

        return sum(self.graph[vertex])

    def getAdjacentVertices(self, vertex) -> list:
        if vertex >= self.dim:
            print("Error: vertex out of range")
            return []

        return [i for i, x in enumerate(self.graph[vertex]) if x == 1]

    def removeVertex(self, vertex: int):
        if vertex >= self.dim:
            print("Error: vertex out of range")
            return

        for i in range(self.dim):
            self.graph[vertex][i] = 0
            self.graph[i][vertex] = 0


class GraphList(Graph):
    def __init__(self, dim: int):
        self.dim = dim
        self.graph = [[] for x in range(dim)]

    def getDim(self) -> int:
        return self.dim

    def addEdge(self, i: int, j: int):
        if i >= self.dim or j >= self.dim:
            print("Error: vertex out of range")
            return

        if j not in self.graph[i]:
            self.graph[i].append(j)
            self.graph[j].append(i)

    def getGraph(self) -> list:
        return self.graph

    def getVertexDegree(self, vertex: int) -> int:
        if vertex >= self.dim:
            print("Error: vertex out of range")
            return 0

        return len(self.graph[vertex])

    def getAdjacentVertices(self, vertex: int) -> list:
        if vertex >= self.dim:
            print("Error: vertex out of range")
            return []

        return self.graph[vertex]

    def removeVertex(self, vertex: int):
        if vertex >= self.dim:
            print("Error: vertex out of range")
            return

        for i in self.graph[vertex]:
            self.graph[i].remove(vertex)
        self.graph[vertex] = []


def readGraph(inputFile: BufferedReader):
    dim = [int(x) for x in next(inputFile).split()][0]
    ret = [dim, [[int(x) for x in line.split()] for line in inputFile]]
    inputFile.close()
    return ret


def createPriorityQueue(graph: Graph) -> PriorityQueue:
    # returns a priority queue with the vertices sorted by degree
    q = PriorityQueue(graph.getDim())
    for i in range(graph.getDim()):
        vertexDegree = graph.getVertexDegree(i)
        if vertexDegree > 0:
            # add the vertex to the queue and set its priority to its degree
            q.put((vertexDegree, i))
    return q


def parseArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--inputFile",
                        type=argparse.FileType('r'), help="Input file")
    parser.add_argument("-m", "--matrix", action="store_true",
                        help="Use matrix representation, default")
    parser.add_argument("-l", "--list", action="store_true",
                        help="Use list representation")
    parser.add_argument(
        "-d", "--DEBUG", action="store_true", help="Debug mode")
    parser.add_argument("-o", "--outputFile", type=argparse.FileType('w'), help= "Output file")
    parser.add_argument("-no-guess", "--no-guess", action="store_true", help= "Do not use the guess, \
        by default the program makes a guess using the algorithm explained in the README.md\nRecomended for small graphs")
    parser.add_argument("-make-guess", "--make-guess", type=int, help= "Takes a guess and checks if there is a solution with \
        that many monitors or less")
    return parser.parse_args()


def createGraph(args: argparse.Namespace) -> Graph:
    # returns a graph object based on the input file

    # read the graph from the input file
    if args.inputFile:
        dim, graph = readGraph(args.inputFile)
    else:
        filePath = input("Enter the path of the input file: ")
        dim, graph = readGraph(open(filePath))

    # choose the graph representation
    if args.list:
        g = GraphList(dim)
    else:
        g = GraphMatrix(dim)

    for i in range(dim):
        for j in range(dim):
            if graph[i][j] == 1:
                g.addEdge(i, j)
    return g


def guessMinCover(g: Graph) -> int:
    # returns a guess for the minimum number of vertices
    # needed to cover the graph

    nrOfVertices = 0
    stop = False
    solution = []

    while not stop:
        # create priority queue with vertices sorted by degree
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
            solution.extend(adjacenctVertices)
    if DEBUG:
        print("guessed solution: ", solution)
    return nrOfVertices


def getCombinations(subsetLength: int, setLength: int) -> list:
    # return all the combinations of subsetLength elements from a set of setLength elements
    output = []

    def dfs(left: int, cur: list):
        if len(cur) == subsetLength:   # finish k items
            output.append(cur[:])
            return
        for i in range(left, setLength):
            cur.append(i)   # pick i
            dfs(i + 1, cur)  # pick next from i+1
            cur.pop()       # reset for next iteration
    dfs(0, [])
    return output


def searchMinCover(g: Graph, guess: int) -> int:
    # returns the minimum number of vertices needed to cover the graph

    # binary search for the minimum number of vertices
    max = guess
    min = 1

    while min < max:
        mid = int((min + max) / 2)
              

        if g.isCovered(mid):
            max = mid
        else:
            if DEBUG:
                print("No solution with ", mid, " vertices\n")
            min = mid + 1
    if DEBUG:
        if max == guess:
            print("No other cover found")
    return max


def main():
    start_time = time.time()
    args = parseArgs()

    if args.DEBUG:
        global DEBUG
        DEBUG = True
    if args.outputFile:
        sys.stdout = args.outputFile

    g = createGraph(args)

    gCopy = copy.deepcopy(g)

    if args.make_guess:
        verticesGuess = args.make_guess
        if verticesGuess > g.getDim() or not g.isCovered(verticesGuess):
            print("The guess is not correct")
            return
    elif not args.no_guess:
        verticesGuess = guessMinCover(gCopy)
        if DEBUG:
            print("guessed number of vertices: ", verticesGuess)
    else:
        verticesGuess = g.getDim()


    print(searchMinCover(g, verticesGuess))

    if DEBUG:
        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
