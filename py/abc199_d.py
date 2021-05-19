N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(M)]
graph = {}
for i in range(1, N+1):
    graph[i] = []

visited = set()


def dfs(visited: set, graph: {}, node):
    if node not in visited:
        nodes.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


for ab in lab:
    a, b = ab[0], ab[1]
    graph[a].append(b)
    graph[b].append(a)

ans = 1
print(graph)
color = [-1]*N
print(color)
for i in range(1, N+1):
    if i in visited:
        continue
    nodes = []
    dfs(visited, graph, i)
    print(nodes)
