Summary

This practical implements Prim's algorithm, a greedy algorithm that finds the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph. An MST connects all vertices with exactly V − 1 edges and the smallest possible total weight, without forming a cycle.

The graph has 6 vertices (A to F) and 9 weighted edges, stored as an adjacency matrix with hardcoded input.
The algorithm starts at vertex A and repeatedly adds the cheapest edge that connects a vertex inside the tree to a vertex outside it.
The key[] array stores the cheapest edge weight linking each vertex to the tree, parent[] stores the tree edge, and in_mst[] marks the vertices already included.
Vertices were added in the order A, C, B, D, E, F, giving the MST edges A-C (2), C-B (1), B-D (5), D-E (2) and E-F (3), with a total weight of 13


Conclusion

Prim's algorithm was successfully implemented and produced a minimum spanning tree of total weight 13 for the sample graph. The tree has V − 1 = 5 edges, connects all vertices and contains no cycle. The algorithm uses the greedy choice of always picking the cheapest edge leaving the current tree, and this choice always leads to an optimal solution. With an adjacency matrix it runs in O(V²), which suits dense graphs, while a min-heap with an adjacency list improves it to O(E log V) for sparse graphs. Prim's algorithm is used in network design problems such as laying cables, pipelines or road networks at minimum cost.