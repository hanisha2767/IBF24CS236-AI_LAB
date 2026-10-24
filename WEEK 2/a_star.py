
import heapq

n = int(input("Enter number of vertices: "))

vertices = []
for i in range(n):
    vertices.append(input("Enter vertex name: "))

print("Enter cost adjacency matrix (0 means no edge):")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

h = list(map(int, input("Enter heuristic values: ").split()))

start = vertices.index(input("Enter start vertex: "))
goal = vertices.index(input("Enter goal vertex: "))

pq = [(h[start], 0, start)]
g_cost = {start: 0}
parent = {start: -1}

while pq:
    f, g, u = heapq.heappop(pq)

    if g != g_cost[u]:
        continue

    if u == goal:
        path = []
        while u != -1:
            path.append(vertices[u])
            u = parent[u]

        path.reverse()
        print("Path:", " -> ".join(path))
        print("Total cost:", g)
        break

    for v in range(n):
        if graph[u][v] > 0:
            new_g = g + graph[u][v]

            if v not in g_cost or new_g < g_cost[v]:
                g_cost[v] = new_g
                parent[v] = u
                new_f = new_g + h[v]
                heapq.heappush(pq, (new_f, new_g, v))

else:
    print("No path found")
