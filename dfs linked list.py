# Node for linked list stack
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack implemented with linked list
class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def is_empty(self):
        return self.top is None


# DFS using only linked list stack
def dfs_iterative(graph, start):
    visited = set()
    stack = LinkedListStack()
    stack.push(start)

    while not stack.is_empty():
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # push neighbors in reverse order to preserve DFS order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.push(neighbor)


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS traversal starting from A:")
dfs_iterative(graph, 'A')
