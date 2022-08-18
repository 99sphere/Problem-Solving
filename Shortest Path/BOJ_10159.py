# BOJ 10159
# Author: Gu Lee
# Date: 2022.08.18
# Source: https://www.acmicpc.net/problem/10159

import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        if graph[a][b] == INF and graph[b][a] == INF:
            cnt += 1
    print(cnt)
