# BOJ 2573
# Author: Gu Lee
# Date: 2022.02.20
# Source: https://www.acmicpc.net/problem/2573

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
year = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check_range(x, y):
  return (0 <= x < n) and (0 <= y < m)
  
def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if check_range(nx, ny) and visited[nx][ny] == False and graph[nx][ny] > 0:
        visited[nx][ny] = True
        queue.append((nx, ny))
  return 1

def melting():
  count = [[0 for _ in range(m)] for _ in range(n)]
  for x in range(n):
    for y in range(m):
      if graph[x][y] > 0:
        cnt = 0
        for k in range(4):
          nx = x + dx[k]
          ny = y + dy[k]
          if check_range(nx, ny) and graph[nx][ny] == 0:
            cnt += 1
        count[x][y] = cnt
  
  for x in range(n):
        for y in range(m):
            graph[x][y] -= count[x][y]
            if graph[x][y] < 0:
                graph[x][y] = 0
        
while True:
  year += 1
  melting()
  visited = [[False for _ in range(m)] for _ in range(n)]
  result = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] > 0 and visited[i][j] == False:
        result += bfs(i, j)

  if result >= 2:
    print(year)
    break

  elif result == 0:
    print(0)
    break
