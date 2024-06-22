from collections import deque

def bfs(graph, start):
    # Initialize a queue for BFS and add the start node to it
    queue = deque([start])
    # Set to keep track of visited nodes
    visited = set([start])
    
    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        print(node, end=" ")

        # Get all adjacent vertices of the dequeued node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # If a neighbor has not been visited, mark it visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting BFS from node 'A'
print("Breadth-First Search starting from node 'A':")
bfs(graph, 'A')
