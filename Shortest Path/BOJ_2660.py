# BOJ 2660
# Author: Gu Lee
# Date: 2022.09.10
# Source: https://www.acmicpc.net/problem/2660

import sys

input = sys.stdin.readline
INF = int(1e9)

if __name__ == "__main__":
    n = int(input())
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        else:
            graph[a][b] = 1
            graph[b][a] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    score = []
    for i in range(1, n+1):
        score.append(max(graph[i][1:]))
    
    target = min(score)
    print(target, score.count(target))

    for i, v in enumerate(score):
        if v == target:
            print(i+1, end = " ")
