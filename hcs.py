import random

def f(x):
    return -x**2

def neighbour_f(x):
    return [x+dx for dx in [-0.1, 0, 0.1]]

x_range = [x for x in range(10)]

def hcs(f, neighbour_f, max_iter=1000):
    n = random.choice(list(x_range))
    for i in range(max_iter):
        neighbours = neighbour_f(n)
        next_neighbour = max(neighbours, key=lambda x: f(x))
        if f(next_neighbour) <= f(n):
            break
        n = next_neighbour
    return n, f(n)

best_solution, best_value = hcs(f, neighbour_f)
print("Best Solution :", best_solution, " Best Value :", best_value)
