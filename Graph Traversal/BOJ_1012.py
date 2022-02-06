# BOJ 1012
# Author: Gu Lee
# Date: 2022.02.06
# Source: https://www.acmicpc.net/problem/1012

from collections import deque

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
        
      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
      
      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        result += 1
        queue.append((nx, ny))

  return result

T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  graph = []
  for ___ in range(N):
    graph.append([0]*M)

  for ____ in range(K):
    y, x = map(int, input().split())
    graph[x][y] = 1

  cnt = 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        bfs(i, j)
        cnt += 1
  print(cnt)
