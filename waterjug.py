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

       from collections import deque

def solve(jug_sizes, target, start):
    cap1, cap2 = jug_sizes
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (j1, j2), path = queue.popleft()

        # ✅ Goal check
        if target in (j1, j2):
            return path

        # 🔁 All possible next moves
        moves = [
            (cap1, j2),             # fill jug1
            (j1, cap2),             # fill jug2
            (0, j2),                # empty jug1
            (j1, 0),                # empty jug2
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),  # pour jug1 → jug2
            (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1))   # pour jug2 → jug1
        ]

        for a, b in moves:
            # 🧠 Easier “zero and limit” check
            if 0 <= a <= cap1 and 0 <= b <= cap2 and (a, b) not in visited:
                visited.add((a, b))
                queue.append(((a, b), path + [(a, b)]))

    return None

    
jugs = (4, 3)
target = 2
start = (0, 0)
path = solve(jugs, target, start)
print("Path:", path)
