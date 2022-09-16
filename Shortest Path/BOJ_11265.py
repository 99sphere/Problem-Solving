# BOJ 11265
# Author: Gu Lee
# Date: 2022.09.16
# Source: https://www.acmicpc.net/problem/11265

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(m):
    a, b, c = map(int, input().split())
    if c >= graph[a-1][b-1]:
        print("Enjoy other party")
    else:
        print("Stay here")
