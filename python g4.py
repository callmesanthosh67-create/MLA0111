import heapq
def greedy_best_first_search(graph, start, goal, h):
    """
    graph: Dictionary where keys are nodes and values are lists of neighbors
    start: Starting node
    goal: Target node
    h: Heuristic dictionary or function h(node)
    """
    open_list = [(h[start], start, [start])]
    visited = set()
    while open_list:
        _, current, path = heapq.heappop(open_list)
        if current == goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(open_list, (h[neighbor], neighbor, path + [neighbor]))
    return None
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}
path = greedy_best_first_search(graph, 'A', 'F', heuristic)
print(f"Path found: {path}")
