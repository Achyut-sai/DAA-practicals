Summary

Kruskal’s algorithm finds the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph using a greedy approach. It sorts all edges by weight and considers them from smallest to largest. An edge is accepted only if its two endpoints are in different components, and it is rejected if it would form a cycle. A Disjoint Set Union (Union-Find) structure with path compression and union by rank performs this cycle check in almost constant time. The algorithm stops once V-1 edges have been selected.


Conclusion

Kruskal’s algorithm correctly produced a minimum spanning tree of weight 13. This matches the result from Prim’s algorithm on the same graph. The two algorithms may choose different edges when weights tie, but the total MST weight is always the same. Kruskal’s picks the cheapest safe edge across the whole graph, while Prim’s grows a single tree from a start vertex. Kruskal’s works best on sparse graphs, where E is small, because its running time depends on sorting the edges. Prim’s with an adjacency matrix, at O(V²), suits dense graphs better. If the graph is disconnected, Kruskal’s produces a minimum spanning forest instead of a single tree.