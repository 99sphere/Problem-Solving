# BOJ 1613
# Author: Gu Lee
# Date: 2022.08.19
# Source: https://www.acmicpc.net/problem/1613

import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

s = int(input())

for i in range(s):
    a, b = map(int, input().split())
    
    if graph[a][b] != INF and graph[b][a] == INF:
        print(-1)
    
    elif graph[a][b] == INF and graph[b][a] == INF:
        print(0)

    else:
        print(1)
