# BOJ 2206
# Author: Gu Lee
# Date: 2022.02.13
# Source: https://www.acmicpc.net/problem/2206

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
  queue = deque()
  queue.append((0, 0, 1))
  visited = [[[0]*2 for _ in range(m)] for __ in range(n)]
  visited[0][0][1] = 1
  while queue:
    x, y, destroy = queue.popleft()

    if x == n-1 and y == m-1:
      return visited[x][y][destroy]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      
      if graph[nx][ny] == 1 and destroy == 1:
        visited[nx][ny][0] = visited[x][y][1] + 1
        queue.append((nx, ny, 0))

      elif graph[nx][ny] == 0 and visited[nx][ny][destroy] == 0:
        visited[nx][ny][destroy] = visited[x][y][destroy] + 1
        queue.append((nx, ny, destroy))
  return -1

print(bfs())

