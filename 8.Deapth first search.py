def dfs_stack(graph, start):
    # Initialize a stack for DFS
    stack = [start]
    # Set to keep track of visited nodes
    visited = set()

    while stack:
        # Pop a node from the stack
        node = stack.pop()
        
        if node not in visited:
            # Mark the node as visited
            visited.add(node)
            print(node, end=" ")

            # Push all unvisited neighbors to the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting DFS from node 'A'
print("Depth-First Search (Stack) starting from node 'A':")
dfs_stack(graph, 'A')
