from queue import PriorityQueue

def ucs(start, goal, graph):
    q = PriorityQueue()
    q.put((0, start, [start]))  # store cost, node, and path
    visited = set()
    
    while not q.empty():
        cc, cg, path = q.get()   # cc = cost, cg = current node, path = path so far
        
        if cg == goal:
            return cc, path   # return both cost and path
        
        if cg in visited:
            continue
        
        visited.add(cg)
        
        for ngh, cost in graph[cg].items():
            if ngh not in visited:
                nc = cc + cost
                q.put((nc, ngh, path + [ngh]))
    
    return float("inf"), []  # if no path found


# ---- User Input ----
graph = {}
n = int(input("Enter the number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    edges = {}
    m = int(input(f"Enter number of neighbors for {node}: "))
    for _ in range(m):
        neighbor = input("Enter neighbor name: ")
        weight = int(input(f"Enter weight from {node} to {neighbor}: "))
        edges[neighbor] = weight
    graph[node] = edges

start = input("Enter start node: ")
goal = input("Enter goal node: ")

cost, path = ucs(start, goal, graph)
if path:
    print(f"Minimum cost from {start} to {goal} = {cost}")
    print("Path:", " -> ".join(path))
else:
    print(f"No path found from {start} to {goal}")