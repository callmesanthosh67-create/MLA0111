def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs_recursive(graph, 'A')
