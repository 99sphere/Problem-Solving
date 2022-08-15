# BOJ 11724
# Author: Gu Lee
# Date: 2022.08.15
# Source: https://www.acmicpc.net/problem/11724

from collections import deque
from collections import defaultdict

import sys

n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
answer= 0
queue = deque()
for i in range(1, len(visited)):
    if visited[i] == False:
        queue.append(i)
        answer += 1
        while queue:
            start = queue.popleft()
            visited[start] = True
            for e in graph[start]:
                if visited[e] == False:
                    queue.append(e)
                    visited[e] = True
print(answer)
