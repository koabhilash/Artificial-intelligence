def is_valid(graph, color_assignment, region, color):
    """Check if it's valid to assign the color to the region."""
    for neighbor in graph[region]:
        if color_assignment.get(neighbor) == color:
            return False
    return True

def color_map(graph, colors, color_assignment, region):
    """Recursively assign colors to the map regions."""
    if region == len(graph):
        return True
    
    # Get the next region to color
    next_region = list(graph.keys())[region]
    
    for color in colors:
        if is_valid(graph, color_assignment, next_region, color):
            color_assignment[next_region] = color
            
            if color_map(graph, colors, color_assignment, region + 1):
                return True
            
            # Backtrack
            del color_assignment[next_region]
    
    return False

def solve_map_coloring(graph, colors):
    """Solve the map coloring problem."""
    color_assignment = {}
    if not color_map(graph, colors, color_assignment, 0):
        return "No solution found"
    return color_assignment

# Define the graph (map) with regions and their neighbors
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['B', 'C', 'D']
}

# Define the colors
colors = ['Red', 'Green', 'Blue']

# Solve the map coloring problem
solution = solve_map_coloring(graph, colors)

print("Color assignment:", solution)
