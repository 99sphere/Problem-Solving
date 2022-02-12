# BOJ 1987
# Author: Gu Lee
# Date: 2022.02.12
# Source: https://www.acmicpc.net/problem/1987

from collections import deque

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
  queue = deque()
  x, y, ans = 0, 0, 1
  queue = set([(x, y, graph[x][y])])
  while queue:
    x, y, path = queue.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]        
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if graph[nx][ny] not in path:
        queue.add((nx, ny, path+graph[nx][ny]))
        ans = max(ans, len(path) + 1) 
  return ans
print(bfs())
