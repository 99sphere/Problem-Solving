# BOJ 2468
# Author: Gu Lee
# Date: 2022.08.17
# Source: https://www.acmicpc.net/problem/2468

import sys
sys.setrecursionlimit(1000000)

def dfs(x, y, rain, visited, map):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0 <= nx < len(visited) and 0 <= ny < len(visited) and visited[ny][nx] == False and map[ny][nx] > rain:
            visited[ny][nx] = True
            dfs(nx, ny, rain, visited, map)
    return

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

max_h = 0
for i in range(n):
    for j in range(n):
        max_h = max(maps[i][j], max_h)

answer = 0
for rain in range(max_h):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and maps[i][j] > rain:
                visited[i][j] = True
                dfs(j, i, rain, visited, maps)
                cnt += 1
    answer = max(answer, cnt)

print(answer)
