import sys
sys.setrecursionlimit(10**7)


def search_nodes(cur, visited, graph):
    #print(cur, connect)
    if cur not in visited:
        visited.add(cur)
        for node in graph[cur]:
            search_nodes(node, visited, graph)
    return connect


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(M)]
visited = set()
graph = {}
for i in range(1, N+1):
    graph[i] = []

for ab in lab:
    a, b = ab[0], ab[1]
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, N+1):
    connect = set()
    if i in visited:
        continue
    search_nodes(i, visited, graph)
    # print(connect)
    cnt += 1

print(cnt-1)
