The folowing is a solution given for the Monitors problem

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
count its "neighbour" and continue with the algorithm.

In input/input.txt we have the example showed in the drawing and the
answear is indeed 4.