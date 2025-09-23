from queue import PriorityQueue

def astar(graph, start, goal, heuristic):
    # Initialize the priority queue and explored set
    q = PriorityQueue()
    q.put((heuristic[start], start))
    explored = set()

    # Initialize the cost and path dictionaries
    cost = {start: 0}
    path = {start: None}

    while not q.empty():
        _, current = q.get()

        if current == goal:
            # Build the path from start to goal
            path_list = [current]
            while path[current] is not None:
                path_list.append(path[current])
                current = path[current]
            path_list.reverse()
            return path_list

        explored.add(current)

        # Expand the neighbors of the current node
        for neighbor in graph[current]:
            new_cost = cost[current] + graph[current][neighbor]
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                q.put((priority, neighbor))
                path[neighbor] = current

    # If the goal is not reached
    return None


# Define the graph
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'D': 15},
    'C': {'D': 20},
    'D': {}
}

# Define the heuristic
heuristic = {
    'A': 15,
    'B': 10,
    'C': 5,
    'D': 0
}

# Test the A* algorithm
start = 'A'
goal = 'D'
path = astar(graph, start, goal, heuristic)
print("Shortest path from", start, "to", goal, ":", path)
