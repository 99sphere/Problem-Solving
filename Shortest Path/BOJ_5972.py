# BOJ 5972
# Author: Gu Lee
# Date: 2022.09.17
# Source: https://www.acmicpc.net/problem/5972

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        cost, now = heapq.heappop(queue)

        if distance[now] < cost:
            continue

        for i in graph[now]:
            val, next = i[1], i[0]
            if cost+val < distance[next]:
                distance[next] = cost + val
                heapq.heappush(queue, (cost + val, next))


n, m = map(int, input().split())
distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)

print(distance[n])
