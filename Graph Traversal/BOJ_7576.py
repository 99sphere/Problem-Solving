# BOJ 7576
# Author: Gu Lee
# Date: 2022.02.12
# Source: https://www.acmicpc.net/problem/7576

from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      queue.append([i,j])

def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
        
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

bfs()

result = 0
fail_flag = 1
for row in graph:
  for elem in row:
    if elem == 0:
      fail_flag = 0    
  result = max(result, max(row))

if fail_flag == 1:
  print(result- 1)
else:
  print(-1)
