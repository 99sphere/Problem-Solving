# BOJ 2644
# Author: Gu Lee
# Date: 2022.08.20
# Source: https://www.acmicpc.net/problem/2644

from collections import deque

n = int(input())
p1, p2 = map(int, input().split())

visited = [False] * (n+1)
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(p1)
visited[p1] = 0
exist = False
while queue:
    current = queue.popleft()
    for next in graph[current]:
        if visited[next] == False:
            val = visited[current] + 1    
            if next == p2:
                print(val)
                exist = True
            queue.append(next)
            visited[next] = val
if not exist:
    print(-1)
