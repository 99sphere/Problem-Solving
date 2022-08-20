# BOJ 1504
# Author: Gu Lee
# Date: 2022.08.20
# Source: https://www.acmicpc.net/problem/1504

from dis import dis
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end):
    distance = [INF] * (n+1)
    distance[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cost, cur_node = heapq.heappop(queue)

        if distance[cur_node] < cost:
            continue

        for n_cost, n_node in graph[cur_node]:
            new_dist = cost + n_cost
            if new_dist < distance[n_node]:
                distance[n_node] = new_dist
                heapq.heappush(queue, (new_dist, n_node))       
    return distance[end]     

if __name__=="__main__":
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    p1, p2 = map(int, input().split())

    cand1 = dijkstra(1, p1) + dijkstra(p1, p2) + dijkstra(p2, n)
    cand2 = dijkstra(1, p2) + dijkstra(p2, p1) + dijkstra(p1, n)
    
    if cand1 >= INF and cand2 >= INF:
        print(-1)
    else:
        print(min(cand1, cand2))
