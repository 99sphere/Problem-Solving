# BOJ 1743
# Author: Gu Lee
# Date: 2022.08.19
# Source: https://www.acmicpc.net/problem/1743

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 1
    
    visited[y][x] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph) and visited[ny][nx] == False and graph[ny][nx] == 1:
            cnt += dfs(ny, nx)
    return cnt


n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

answer = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            answer.append(dfs(i, j))
print(max(answer))
