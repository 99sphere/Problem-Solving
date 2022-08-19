# BOJ 1956
# Author: Gu Lee
# Date: 2022.08.19
# Source: https://www.acmicpc.net/problem/1956

import sys
input = sys.stdin.readline

INF = int(1e9)

if __name__=="__main__":
    v, e = map(int, input().split())
    graph = [[INF] * v for _ in range(v)]

    for i in range(e):
        start, end, cost = map(int, input().split())
        graph[start-1][end-1] = cost

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]

    cand = [graph[i][i] for i in range(v)]
    answer = min(cand)
    if answer == INF:
        print(-1)
    else:
        print(answer)
