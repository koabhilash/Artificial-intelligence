import heapq

class PuzzleState:
    def __init__(self, board, goal, cost=0, depth=0, parent=None):
        self.board = board
        self.goal = goal
        self.cost = cost
        self.depth = depth
        self.parent = parent

    def __eq__(self, other):
        return self.board == other.board

    def __lt__(self, other):
        return self.cost < other.cost

    def get_blank_pos(self):
        return self.board.index(0)

    def is_goal(self):
        return self.board == self.goal

    def get_neighbors(self):
        neighbors = []
        blank_pos = self.get_blank_pos()
        row, col = divmod(blank_pos, 3)
        
        directions = {'up': -3, 'down': 3, 'left': -1, 'right': 1}
        for direction, delta in directions.items():
            new_blank_pos = blank_pos + delta
            if direction == 'up' and row == 0:
                continue
            if direction == 'down' and row == 2:
                continue
            if direction == 'left' and col == 0:
                continue
            if direction == 'right' and col == 2:
                continue

            new_board = self.board[:]
            new_board[blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[blank_pos]
            neighbors.append(PuzzleState(new_board, self.goal, self.cost + 1, self.depth + 1, self))
        
        return neighbors

    def manhattan_distance(self):
        distance = 0
        for i in range(1, 9):
            current_pos = self.board.index(i)
            goal_pos = self.goal.index(i)
            current_row, current_col = divmod(current_pos, 3)
            goal_row, goal_col = divmod(goal_pos, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def total_cost(self):
        return self.depth + self.manhattan_distance()

def a_star_search(start_state):
    open_set = []
    heapq.heappush(open_set, (start_state.total_cost(), start_state))
    closed_set = set()

    while open_set:
        _, current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            return reconstruct_path(current_state)

        closed_set.add(tuple(current_state.board))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) in closed_set:
                continue

            heapq.heappush(open_set, (neighbor.total_cost(), neighbor))

    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()

if __name__ == "__main__":
    initial_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initial_state = PuzzleState(initial_board, goal_board)
    solution = a_star_search(initial_state)

    if solution:
        print("Solution found!")
        for step in solution:
            print_board(step)
    else:
        print("No solution exists.")
