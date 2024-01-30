class SearchNode:
    def __init__(self, state, cost, path=[]):
        self.state = state
        self.cost = cost
        self.path = path

def get_neighbors(state):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for direction in directions:
        neighbor = (state[0] + direction[0], state[1] + direction[1])
        if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] != '%':
            cost = 2 if grid[neighbor[0]][neighbor[1]] == '%' else 1
            neighbors.append((neighbor, cost))

    return neighbors

def ida_star_search(start, goal):
    threshold = heuristic(start, goal)

    while True:
        result, new_threshold = dfs_a_star(start, goal, 0, threshold, set())

        if result[0] == 'FOUND':
            return result[1]
        if new_threshold == float('inf'):
            return None

        threshold = new_threshold

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def dfs_a_star(current, goal, cost, threshold, visited):
    f = cost + heuristic(current, goal)

    if f > threshold:
        return ('CUTOFF', f)

    if current == goal:
        return ('FOUND', cost)

    min_val = float('inf')
    min_path = []

    for neighbor, step_cost in get_neighbors(current):
        if neighbor not in visited:
            visited.add(neighbor)
            result, new_threshold = dfs_a_star(neighbor, goal, cost + step_cost, threshold, visited)

            if result[0] == 'FOUND':
                return ('FOUND', result[1])
            if new_threshold < min_val:
                min_val = new_threshold
                min_path = result[1]

    return ('CUTOFF', min_val, min_path)

# Example usage:
grid = [
    "%%%%%%%",
    "%    .%",
    "% %%%%%",
    "%     %",
    "%%%% %%",
    "%A    %",
    "%%%%%%%"
]

start = (5, 1)  # A's initial position
goal = (1, 5)   # Goal position

result = ida_star_search(start, goal)

if result is None:
    print("No path found.")
else:
    print("Path found:")
    for step in result:
        print(step)
