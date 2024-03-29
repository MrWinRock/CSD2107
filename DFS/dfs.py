def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)

# Example usage:
graph_example = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B'},
    'F': {'C'},
    'G': {'C'}
}

dfs(graph_example, 'A')
