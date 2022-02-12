# BOJ 7569
# Author: Gu Lee
# Date: 2022.02.12
# Source: https://www.acmicpc.net/problem/7569

from collections import deque

m, n, h = map(int, input().split())

graph = []
for i in range(h):
  floor = []
  for j in range(n):
    floor.append(list(map(int, input().split())))
  graph.append(floor)

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

queue = deque()
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 1:
        queue.append((i,j,k))
        
def bfs():
  while queue:
    z, x, y = queue.popleft()
    for i in range(6):
      nz = z + dz[i]
      nx = x + dx[i]
      ny = y + dy[i]
        
      if nz < 0 or nx < 0 or ny < 0 or nz >= h or nx >= n or ny >= m:
        continue

      if graph[nz][nx][ny] == 0:
        graph[nz][nx][ny] = graph[z][x][y] + 1
        queue.append((nz, nx, ny))

bfs()

result = 0
fail_flag = 1
for floor in graph:
  for row in floor:
    for elem in row:
      if elem == 0:
        fail_flag = 0    
    result = max(result, max(row))

if fail_flag == 1:
  print(result- 1)
else:
  print(-1)
