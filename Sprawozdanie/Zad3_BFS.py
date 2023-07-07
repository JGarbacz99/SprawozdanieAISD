from collections import deque

def BFS(graph, s):
    visited = set()
    queue = deque([s])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            neighbors = graph[vertex]
            queue.extend(neighbors)
graph ={
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}
start = 'A'
print("BFS: ")
BFS(graph, start)
