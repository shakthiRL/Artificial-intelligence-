def is_safe(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def solve(node, graph, colors, num_colors):
    if node == len(graph):
        return True

    for color in range(num_colors):
        if is_safe(node, color, graph, colors):
            colors[node] = color
            if solve(node + 1, graph, colors, num_colors):
                return True
            colors[node] = -1
    return False

def map_coloring(graph, num_colors):
    colors = [-1] * len(graph)
    if solve(0, graph, colors, num_colors):
        return colors
    else:
        return None

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

num_colors = 3

result = map_coloring(graph, num_colors)
if result:
    print("Colors assigned to nodes:", result)
else:
    print("No solution exists.")
