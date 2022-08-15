# BOJ 2606
# Author: Gu Lee
# Date: 2022.08.15
# Source: https://www.acmicpc.net/problem/2606


def dfs(i, graph, visited):
    visited[i] = True
    for (start, end) in graph:
        if start == i and visited[end] == False:
            dfs(end, graph, visited)
    return

t = int(input())
n = int(input())

visited = [False] * t
graph = []
for i in range(n):
    a, b = map(int, input().split())
    graph.append([a-1, b-1])
    graph.append([b-1, a-1])

dfs(0, graph, visited)

answer = 0
for val in visited:
    if val:
        answer += 1
print(answer - 1)
