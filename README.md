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
    The program makes a guess for the solution and then uses binary search to find if there is 
    a better one(with less vertices)

    3.1) The guess
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

    3.2) Binary search
        The program takes the guess and looks for a smaller number (of vertices) that
        can cover that graph. It checks every possible combination of k vertices, where
        k is the smaller number.

    3.1) Matrix implementation (default)(-m)

    *3.2) List implementation (-l)



    In input/input1.txt there is the example showed in the drawing and the
    answer is indeed 4.

*The implementations matters only for the script itself, the input should always be 
an adjacency matrix

4) options:
  -h, --help            show this help message and exit
  -f INPUTFILE, --inputFile INPUTFILE
                        Input file
  -m, --matrix          Use matrix representation, default
  -l, --list            Use list representation
  -d, --DEBUG           Debug mode
  -o OUTPUTFILE, --outputFile OUTPUTFILE
                        Output file
  -no-guess, --no-guess
                        Do not use the guess, by default the program makes a guess using the algorithm explained in the README.md Recomended for    
                        small graphs
  -make-guess MAKE_GUESS, --make-guess MAKE_GUESS
                        Takes a guess and checks if there is a solution with that many monitors or less