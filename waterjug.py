from collections import deque

def solve(jug_sizes, target, start):
    c1, c2 = jug_sizes
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (j1, j2), path = queue.popleft()

        # ✅ Goal check
        if target in (j1, j2):
            return path

        # 🔁 All possible next moves
        moves = [
            (c1, j2), (j1, c2),           # fill each jug
            (0, j2), (j1, 0),             # empty each jug
            (j1 - min(j1, c2 - j2), j2 + min(j1, c2 - j2)),  # pour j1 → j2
            (j1 + min(j2, c1 - j1), j2 - min(j2, c1 - j1))   # pour j2 → j1
        ]

        for next_state in moves:
            if next_state not in visited and all(0 <= x <= y for x, y in zip(next_state, (c1, c2))):
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None
jugs = (4, 3)
target = 2
start = (0, 0)
path = solve(jugs, target, start)
print("Path:", path)
