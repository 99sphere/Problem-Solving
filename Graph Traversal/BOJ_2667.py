# BOJ 2667
# Author: Gu Lee
# Date: 2022.02.06
# Source: https://www.acmicpc.net/problem/2667

from collections import deque

n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 0
  result = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
        
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      
      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        result += 1
        queue.append((nx, ny))

  return result

results = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      results.append(bfs(i, j))
      
results = sorted(results)
print(len(results))
for i in range(len(results)):
  print(results[i])
