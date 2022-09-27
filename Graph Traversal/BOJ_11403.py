# BOJ 11403
# Author: Gu Lee
# Date: 2022.09.27
# Source: https://www.acmicpc.net/problem/11403

from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]


def bfs(start, end):
    visited = [False] * n
    queue = deque()
    queue.append(start)
    #visited[start] = True

    while queue:
        current = queue.popleft()
        for idx, val in enumerate(graph[current]):
            if val and visited[idx]==False:
                queue.append(idx)
                visited[idx] = True

                if idx == end:
                    return "1"

    return "0"

for i in range(n):
    for j in range(n):
        answer[i][j] = bfs(i, j)

for ans in answer:
    print(" ".join(ans))
