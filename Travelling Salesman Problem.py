import itertools

def tsp_brute_force(graph):
    min_cost = float('inf')
    min_path = None
    n = len(graph)

    for perm in itertools.permutations(range(1, n)):
        current_cost = graph[0][perm[0]]  
        for i in range(len(perm) - 1):
            current_cost += graph[perm[i]][perm[i+1]]  
        current_cost += graph[perm[-1]][0]  
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = [0] + list(perm) + [0]

    return min_path, min_cost

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_path, min_cost = tsp_brute_force(graph)
print("Minimum Cost Path:", min_path)
print("Minimum Cost:", min_cost)
