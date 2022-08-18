# BOJ 18352
# Author: Gu Lee
# Date: 2022.08.18
# Source: https://www.acmicpc.net/problem/18352

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        dist, current_node = heapq.heappop(queue)
        for node, cost in graph[current_node]:
            new_dist = dist + cost

            if new_dist < distance[node]:
                distance[node] = new_dist
                heapq.heappush(queue, (new_dist, node))

if __name__ == "__main__":
    n, m, k, start = map(int, input().split())

    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append((b, 1))

    dijkstra(start)

    cnt = 0
    for i, val in enumerate(distance):
        if val == k:
            cnt = 1
            print(i)

    if cnt == 0:
        print(-1)
