# BOJ 21736
# Author: Gu Lee
# Date: 2022.09.10
# Source: https://www.acmicpc.net/problem/21736

import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0
def dfs(x, y):
    global ans
    visited[y][x] = True
    if graph[y][x] == "P":
        ans += 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False and graph[ny][nx] != "X":
            dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            dfs(j, i)

if ans:
    print(ans)
else:
    print("TT")
