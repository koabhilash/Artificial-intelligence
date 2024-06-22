from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if self.missionaries < 3 and (3 - self.missionaries) < (3 - self.cannibals):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def get_neighbors(self):
        neighbors = []
        if self.boat == 1:  # Boat on the original side
            for m, c in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
                new_state = State(self.missionaries - m, self.cannibals - c, 0, self)
                if new_state.is_valid():
                    neighbors.append(new_state)
        else:  # Boat on the opposite side
            for m, c in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
                new_state = State(self.missionaries + m, self.cannibals + c, 1, self)
                if new_state.is_valid():
                    neighbors.append(new_state)
        return neighbors

    def __eq__(self, other):
        return (self.missionaries, self.cannibals, self.boat) == (other.missionaries, other.cannibals, other.boat)

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def bfs(start_state):
    queue = deque([start_state])
    visited = set()
    visited.add(start_state)

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return reconstruct_path(current_state)

        for neighbor in current_state.get_neighbors():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    return path[::-1]

def print_state(state):
    print(f"({state.missionaries}, {state.cannibals}, {state.boat})")

if __name__ == "__main__":
    start_state = State(3, 3, 1)
    solution = bfs(start_state)

    if solution:
        print("Solution found!")
        for step in solution:
            print_state(step)
    else:
        print("No solution exists.")
