from collections import deque
def BFS(a, b, target):
    m = {}
    isSolvable = False
    path = []
    q = deque()
    q.append((0, 0))

    while len(q) > 0:
        u = q.popleft()

        # If this state is already visited
        if (u[0], u[1]) in m:
            continue

        # If any of the jugs has more water than its capacity or less than 0, skip this state
        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue

        # Add this state to the path
        path.append([u[0], u[1]])

        # Mark this state as visited
        m[(u[0], u[1])] = 1

        # If we reach the target, print the solution
        if u[0] == target or u[1] == target:
            isSolvable = True
            if u[0] == target and u[1] != 0:
                path.append([u[0], 0])
            elif u[1] == target and u[0] != 0:
                path.append([0, u[1]])
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",", path[i][1], ")")
            break

        # Add the next possible states
        q.append((u[0], b))  # Fill Jug2
        q.append((a, u[1]))  # Fill Jug1

        for ap in range(max(a, b) + 1):
            # Pour water from Jug2 to Jug1
            c = u[0] + ap
            d = u[1] - ap
            if c == a or (d == 0 and d >= 0):
                q.append((c, d))

            # Pour water from Jug1 to Jug2
            c = u[0] - ap
            d = u[1] + ap
            if (c == 0 and c >= 0) or d == b:
                q.append((c, d))

        q.append((a, 0))  # Empty Jug1
        q.append((0, b))  # Empty Jug2

    if not isSolvable:
        print("No solution")

if __name__ == "__main__":
    Jug1, Jug2, target = 4, 3, 2
    print("Path from initial state to solution state ::")
    BFS(Jug1, Jug2, target)
