# BOJ 1697
# Author: Gu Lee
# Date: 2022.08.15
# Source: https://www.acmicpc.net/problem/1697

from collections import deque

n, k = map(int, input().split())
queue = deque([])
dist = [0] * 1000001
queue.append(n)

while queue:
    pos = queue.popleft()
    if pos == k:
        print(dist[pos])
        break
    for n_pos in [pos-1, pos+1, pos*2]:
        if 0 <= n_pos <= 100000 and dist[n_pos] == 0:
            queue.append(n_pos)
            dist[n_pos] = dist[pos] + 1
