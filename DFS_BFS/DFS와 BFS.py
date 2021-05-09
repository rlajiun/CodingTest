from collections import deque

def dfs(graph, node, visited):
  visited[node] = 1
  print(node, end=' ')
  try:
    graph[node].sort()
    for g in graph[node]:
      if not visited[g]: dfs(graph, g, visited)
  except: return

def bfs(graph, start, visited):
  q = deque([start])
  visited[start] = 1

  while q:
    node = q.popleft()
    print(node, end=' ')
    try:
      graph[node].sort()
      for g in graph[node]:
        if not visited[g]: 
          q.append(g)
          visited[g] = 1
    except: return

N, M, V = map(int, input().split())
graph = {}
for i in range(M):
  j, k = map(int, input().split())
  if j not in graph: graph[j] = [k]
  else: graph[j].append(k)
  if k not in graph: graph[k] = [j]
  else: graph[k].append(j)
visited = [0]*(N+1)
dfs(graph, V, visited)
print()
visited = [0]*(N+1)
bfs(graph, V, visited)
# https://www.acmicpc.net/problem/1260
