# BOJ 1446
# Author: Gu Lee
# Date: 2022.08.19
# Source: https://www.acmicpc.net/problem/1446

from dis import dis
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cost, node = heapq.heappop(queue)

        for dist, next in graph[node]:
            new_cost = cost + dist
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(queue, (new_cost, next))

if __name__ == "__main__":
    n, d = map(int, input().split())

    distance = [INF] * (d+1)

    graph = [[] for _ in range(d+1)]
    for i in range(n):
        a, b, c = map(int, input().split())
        if b <= d:
            graph[a].append((c, b))

    for i in range(d):
        graph[i].append((1, i+1))

    dijkstra(0)
    answer = 0
    shortcut_end = 0
    for i, dist in enumerate(distance):
        if dist != INF:
            answer = dist
            shortcut_end = i
    
    print(distance[-1])