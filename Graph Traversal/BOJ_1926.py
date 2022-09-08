# BOJ 1926
# Author: Gu Lee
# Date: 2022.08.19
# Source: https://www.acmicpc.net/problem/1926

import sys
from collections import deque

sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cand = []

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] == 1:
            queue = deque()
            queue.append([j,i])
            visited[i][j] = True
            ans = 1
            while queue:
                node = queue.popleft()
                x = node[0]
                y = node[1]
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False and graph[ny][nx] == 1:
                        ans += 1
                        visited[ny][nx] = True
                        queue.append([nx, ny])
            cand.append(ans)

print(len(cand))
if not cand:
    print(0)
else:
    print(max(cand))