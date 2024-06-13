#Done by M Harish AIML-A 231501058
def water_jug_dfs(capacity_x, capacity_y, target):
    def dfs(x, y, path):
        if x == target or y == target:
            path.append((x, y))
            return True
        if visited[x][y]:
            return False
        visited[x][y] = True

        if x < capacity_x:  # Fill Jug X
            if dfs(capacity_x, y, path):
                path.append((x, y))
                return True
        if y < capacity_y:  # Fill Jug Y
            if dfs(x, capacity_y, path):
                path.append((x, y))
                return True
        if x > 0:  # Empty Jug X
            if dfs(0, y, path):
                path.append((x, y))
                return True
        if y > 0:  # Empty Jug Y
            if dfs(x, 0, path):
                path.append((x, y))
                return True
        if x > 0 and y < capacity_y:  # Pour water from Jug X to Jug Y
            pour = min(x, capacity_y - y)
            if dfs(x - pour, y + pour, path):
                path.append((x, y))
                return True
        if y > 0 and x < capacity_x:  # Pour water from Jug Y to Jug X
            pour = min(y, capacity_x - x)
            if dfs(x + pour, y - pour, path):
                path.append((x, y))
                return True

        return False

    visited = [[False for _ in range(capacity_y + 1)] for _ in range(capacity_x + 1)]
    path = []

    if dfs(0, 0, path):
        path.reverse()
        return path
    else:
        return "No solution found."

capacity_x = 4
capacity_y = 3
target = 2

solution_path = water_jug_dfs(capacity_x, capacity_y, target)
if solution_path != "No solution found.":
    for step, (x, y) in enumerate(solution_path):
        print(f"Step {step}: Jug X: {x}, Jug Y: {y}")
else:
    print("No solution found.")

#Done by M Harish AIML-A 231501058