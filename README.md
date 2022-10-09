0) Use -h or --help for list of possible arguments.

1) Input (if the file isn't given as argument):
    The programs take as input a path to a file.

    1.1) Input file documentation:
        The input file should have the dimension of the graph on the first line and
        the graph represented as an adjacency matrix on the next lines
        
    1.2) Example inputs are given in the "input/" directory.


2) Output:
   The program will write in console the least amount of vertices required to cover all
   edges

3) Implementation:
    (easy to watch on the example in /images)

    Say we have a undirected graph. To find the minimum number of veritces we first
    take the vertex with the lowest degree(least edges). To cover all its edges we
    need all of its adjacent vertices so we count all of them for the final result.

    In the example, we take the vertex numbered (1) as it has the least number of 
    edges (only 1) and count its adjacent vertices (the vertex crossed in red).
    Now we can eliminate all its edges (of the vertex crossed)(showed by red 
    lines).

    We repeat the same process after we eliminated the edges until there are no
    more edges in the graph.

    Next, we see that the vertex numbered (2) has only 1 edge remaining. We
    count its "neighbour(s)" and continue with the algorithm..

    3.1) Matrix implementation (default)(-m)

    *3.2) List implementation (-l)



    In input/input1.txt there is the example showed in the drawing and the
    answear is indeed 4.

*The implementations matters only for the script itself, the input should always be 
an adjacency matrix