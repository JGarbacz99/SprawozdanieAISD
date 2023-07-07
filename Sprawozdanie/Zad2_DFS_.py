def DFS(graph, s):
    visited = []
    stack = []

    visited.append(s)
    stack.append(s)

    while stack:
        k = stack.pop()
        print(k, end = " ")

        for n in reversed(graph[k]):
            if n not in visited:
                visited.append(n)
                stack.append(n)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['E'],
    'E': []
}
start = 'A'
DFS(graph, start)