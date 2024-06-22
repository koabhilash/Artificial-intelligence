from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target_amount):
    # To keep track of visited states
    visited = set()
    # Queue for BFS
    queue = deque()
    
    # Starting state (both jugs are empty)
    queue.append((0, 0))
    visited.add((0, 0))
    
    while queue:
        jug1, jug2 = queue.popleft()
        
        # Check if we have reached the target amount in either jug
        if jug1 == target_amount or jug2 == target_amount:
            return True
        
        # Possible next states
        next_states = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  # Pour jug1 to jug2
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   # Pour jug2 to jug1
        ]
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    
    return False

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

if water_jug_bfs(jug1_capacity, jug2_capacity, target_amount):
    print(f"Yes, it is possible to measure {target_amount} liters.")
else:
    print(f"No, it is not possible to measure {target_amount} liters.")
