from itertools import permutations

# Define the distance matrix
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Number of cities
num_cities = len(distance_matrix)

# Function to calculate the total distance of a given tour
def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i+1]]
    total_distance += distance_matrix[tour[-1]][tour[0]]  # return to starting city
    return total_distance

# Generate all possible tours
all_possible_tours = permutations(range(num_cities))

# Initialize minimum distance to a very large value
min_distance = float('inf')
best_tour = None

# Evaluate each tour
for tour in all_possible_tours:
    current_distance = calculate_total_distance(tour, distance_matrix)
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = tour

# Output the best tour and its distance
print("Best tour:", best_tour)
print("Minimum distance:", min_distance)
