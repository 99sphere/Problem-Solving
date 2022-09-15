# BOJ 11779
# Author: Gu Lee
# Date: 2022.09.15  
# Source: https://www.acmicpc.net/problem/11779

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            next, val = i[0], i[1]
            cost = dist + val
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))
                path[next] = []
                for p in path[now]:
                    path[next].append(p)
                path[next].append(next)

n = int(input())
m = int(input())

path = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

city_A, city_B = map(int, input().split())

path[city_A].append(city_A)

dijkstra(city_A)

print(distance[city_B])
print(len(path[city_B]))
print(" ".join(map(str, path[city_B])))

