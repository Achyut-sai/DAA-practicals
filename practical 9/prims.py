# Practical 9: Prim's Algorithm (Minimum Spanning Tree)

INF = 999999

vertices = ['A', 'B', 'C', 'D', 'E', 'F']

# Adjacency matrix (0 means no edge)
#            A   B   C   D   E   F
graph = [
    [0,  4,  2,  0,  0,  0],   # A
    [4,  0,  1,  5,  0,  0],   # B
    [2,  1,  0,  8, 10,  0],   # C
    [0,  5,  8,  0,  2,  6],   # D
    [0,  0, 10,  2,  0,  3],   # E
    [0,  0,  0,  6,  3,  0],   # F
]


def prim(graph, start=0):
    V = len(graph)
    key = [INF] * V           # smallest edge weight connecting vertex to the tree
    parent = [-1] * V         # parent of each vertex in the MST
    in_mst = [False] * V
    key[start] = 0

    mst_edges = []
    total_weight = 0

    for step in range(V):
        # Pick the vertex with the minimum key that is not yet in the MST
        u = -1
        min_key = INF
        for v in range(V):
            if not in_mst[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        in_mst[u] = True

        # Record the edge used to bring u into the tree
        if parent[u] != -1:
            mst_edges.append((parent[u], u, graph[parent[u]][u]))
            total_weight += graph[parent[u]][u]
            print(f"Step {step}: add vertex {vertices[u]} via edge "
                  f"{vertices[parent[u]]}-{vertices[u]} (weight {graph[parent[u]][u]})")
        else:
            print(f"Step {step}: start with vertex {vertices[u]}")

        # Update keys of the neighbours of u
        for v in range(V):
            if graph[u][v] != 0 and not in_mst[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return mst_edges, total_weight


print("=" * 55)
print("        PRIM'S ALGORITHM (MINIMUM SPANNING TREE)")
print("=" * 55)
print("""
Graph:
         4
    A ------- B
    |       / |
  2 |    1 /  | 5
    |    /    |
    C ------- D
    |  8    / |
 10 |    2 /  | 6
    |    /    |
    E ------- F
         3
""")

print("Adjacency Matrix:")
print("     " + "   ".join(vertices))
for i in range(len(vertices)):
    print(f"  {vertices[i]} " + " ".join(f"{graph[i][j]:3d}" for j in range(len(vertices))))

print("\nConstruction of MST (start vertex A):\n")
edges, total = prim(graph, 0)

print("\nEdges in the Minimum Spanning Tree:")
print(f"{'Edge':<10}{'Weight':<10}")
for u, v, w in edges:
    print(f"{vertices[u]}-{vertices[v]:<8}{w:<10}")

print(f"\nTotal weight of MST : {total}")

V = len(graph)
E = sum(1 for i in range(V) for j in range(i + 1, V) if graph[i][j] != 0)
print("\n" + "-" * 55)
print(f"Vertices (V) = {V}, Edges (E) = {E}, MST edges = {len(edges)} (V - 1)")
print("Time Complexity  : O(V^2)  (adjacency matrix)")
print("                   O(E log V) with a min-heap + adjacency list")
print("Space Complexity : O(V)  (key, parent, in_mst arrays)")
print("-" * 55)