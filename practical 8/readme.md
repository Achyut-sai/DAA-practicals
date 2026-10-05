Summary

This practical implements the two basic graph traversal (searching) algorithms, Breadth First Search (BFS) and Depth First Search (DFS), on the same undirected graph with 6 vertices (A to F) and 6 edges. The graph is stored as an adjacency list (a dictionary mapping each vertex to its neighbours).

BFS starts at vertex A and explores all neighbours of a vertex before moving to the next level. It uses a queue (FIFO) and a visited list. The traversal order was A → B → C → D → E → F, and the program also records each vertex's level (distance from A): B and C are at distance 1, while D, E and F are at distance 2.

DFS starts at A and goes as deep as possible along a branch before backtracking. It was implemented both recursively (using the call stack) and iteratively (using an explicit stack, LIFO). Both versions gave the same order: A → B → D → E → F → C.


Conclusion

BFS and DFS were successfully implemented and tested on a sample graph. Both visited every vertex exactly once, but in different orders: BFS moved level by level, while DFS moved deep along a path before backtracking. Both run in O(V + E) time and O(V) space when the graph is stored as an adjacency list. BFS is the better choice when the shortest path in an unweighted graph or the nearest nodes are needed, while DFS is better suited to cycle detection, topological sorting, finding connected components and exploring all possible paths.