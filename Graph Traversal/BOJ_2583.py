# BOJ 2583
# Author: Gu Lee
# Date: 2022.08.15
# Source: https://www.acmicpc.net/problem/2583

import sys

sys.setrecursionlimit(20000)

def dfs(i, j, graph, val):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[i][j] = 1
    for num in range(4):
        nx = j + dx[num]
        ny = i + dy[num]
        if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph) and graph[ny][nx] == 0:
            val = dfs(ny, nx, graph, val+1)
    return val


n, m, k= map(int, input().split())
rectangles = []
for i in range(k):
    l_x, l_y, r_x, r_y = map(int, input().split())
    rectangles.append([l_x, l_y, r_x, r_y])

graph = [[0]*m for _ in range(n)]

for (l_x, l_y, r_x, r_y) in rectangles:
    for i in range(l_y, r_y):
        for j in range(l_x, r_x):
            graph[i][j] = -1
answer = 0
sizes = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer += 1
            size = dfs(i, j, graph, 1)
            sizes.append(size)
print(answer)
for i in sorted(sizes):
    print(i, end=" ")
print()
