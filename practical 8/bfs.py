# Practical 8(a): Breadth First Search (BFS)

# Graph as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def bfs(graph, start):
    visited = [start]          # order of visiting
    queue = [start]            # FIFO queue
    level = {start: 0}         # distance from start (edges)
    front = 0                  # index of queue front (avoids slow pop(0))

    while front < len(queue):
        node = queue[front]
        front += 1
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                level[neighbour] = level[node] + 1
    return visited, level


print("=" * 50)
print("        BREADTH FIRST SEARCH (BFS)")
print("=" * 50)
print("""
Graph:
          A
         / \\
        B   C
       / \\   \\
      D   E---F
""")

print("Adjacency List:")
for vertex in graph:
    print(f"  {vertex} -> {graph[vertex]}")

start = 'A'
order, level = bfs(graph, start)

print(f"\nStarting vertex : {start}")
print(f"BFS Traversal   : {' -> '.join(order)}")

print("\nLevel (distance from start):")
for vertex in order:
    print(f"  {vertex} : {level[vertex]}")

V = len(graph)
E = sum(len(v) for v in graph.values()) // 2
print("\n" + "-" * 50)
print(f"Vertices (V) = {V}, Edges (E) = {E}")
print("Time Complexity  : O(V + E)")
print("Space Complexity : O(V)  (queue + visited list)")
print("-" * 50)