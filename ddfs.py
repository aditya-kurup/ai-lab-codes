from collections import deque

def dfs_iterative(graph, start):
    visited = set()
    stack = deque([start])
    order = []

    while stack:
        node = stack.pop()   # pop from right → stack behavior
        if node not in visited:
            visited.add(node)
            order.append(node)
            # push neighbors individually in reverse order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(dfs_iterative(graph,'A'))