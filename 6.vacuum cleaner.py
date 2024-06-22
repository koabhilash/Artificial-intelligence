import random

# Define the environment
class Environment:
    def __init__(self, width, height, dirt_probability=0.2):
        self.width = width
        self.height = height
        self.grid = self.initialize_grid(dirt_probability)
    
    def initialize_grid(self, dirt_probability):
        return [[random.random() < dirt_probability for _ in range(self.width)] for _ in range(self.height)]
    
    def is_dirty(self, x, y):
        return self.grid[y][x]
    
    def clean(self, x, y):
        self.grid[y][x] = False
    
    def display(self):
        for row in self.grid:
            print(''.join(['D' if cell else '.' for cell in row]))

# Define the vacuum cleaner agent
class VacuumCleanerAgent:
    def __init__(self, env):
        self.env = env
        self.x = random.randint(0, env.width - 1)
        self.y = random.randint(0, env.height - 1)
    
    def perceive_and_act(self):
        if self.env.is_dirty(self.x, self.y):
            self.env.clean(self.x, self.y)
            print(f'Cleaned cell ({self.x}, {self.y})')
        else:
            self.move()
    
    def move(self):
        move_direction = random.choice(['up', 'down', 'left', 'right'])
        if move_direction == 'up' and self.y > 0:
            self.y -= 1
        elif move_direction == 'down' and self.y < self.env.height - 1:
            self.y += 1
        elif move_direction == 'left' and self.x > 0:
            self.x -= 1
        elif move_direction == 'right' and self.x < self.env.width - 1:
            self.x += 1
        print(f'Moved to ({self.x}, {self.y})')

# Main function to run the simulation
def run_simulation(width, height, dirt_probability, steps):
    env = Environment(width, height, dirt_probability)
    agent = VacuumCleanerAgent(env)
    
    print("Initial Environment:")
    env.display()
    print()
    
    for step in range(steps):
        agent.perceive_and_act()
        print(f"Step {step + 1}:")
        env.display()
        print()

# Parameters
width = 5
height = 5
dirt_probability = 0.2
steps = 20

# Run the simulation
run_simulation(width, height, dirt_probability, steps)
