# BOJ 1916
# Author: Gu Lee
# Date: 2022.08.19
# Source: https://www.acmicpc.net/problem/1916

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, current = heapq.heappop(queue)

        if distance[current] < dist:
            continue
        
        for cost, node in graph[current]:
            new_dist = dist + cost
            if new_dist < distance[node]:
                distance[node] = new_dist
                heapq.heappush(queue, (new_dist, node))


if __name__=="__main__":
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n+1)] 
    distance = [INF] * (n+1)
    for i in range(m):
        start, end, cost = map(int, input().split())
        graph[start].append((cost, end))
    start, end = map(int, input().split())
    dijkstra(start)
    print(distance[end])
