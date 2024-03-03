import heapq

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(start, goal, graph):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2)],
    (0, 2): [(0, 1), (1, 2)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(1, 0), (1, 2)],
    (1, 2): [(0, 2), (1, 1)]
}

start_node = (0, 0)
goal_node = (1, 2)

path = astar(start_node, goal_node, graph)
print("Path from", start_node, "to", goal_node, ":", path)
