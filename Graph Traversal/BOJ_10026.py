# BOJ 10026
# Author: Gu Lee
# Date: 2022.02.12
# Source: https://www.acmicpc.net/problem/10026

from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  queue.append((x,y))
  visited.append((x,y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
        
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue

      if (nx, ny) not in visited and graph[nx][ny] == graph[x][y]:
        queue.append((nx, ny))
        visited.append((nx, ny))

queue = deque()
visited = []
result1 = 0
for i in range(n):
  for j in range(n):
    if (i,j) not in visited:
      bfs(i,j)
      result1 += 1  

for i in range(n):
  for j in range(n):
    if graph[i][j] == 'G':
      graph[i][j] = 'R'

queue = deque()
visited = []
result2 = 0
for i in range(n):
  for j in range(n):
    if (i,j) not in visited:
      bfs(i,j)
      result2 += 1

print(result1, result2)  
