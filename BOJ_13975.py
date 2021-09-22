# BOJ 13975
# Author: Gu Lee
# Date: 2021.09.22
# Source: https://www.acmicpc.net/problem/13975

import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cost = list(map(int, input().split()))
    heapq.heapify(cost)
    result = 0
    while True:
        first = heapq.heappop(cost)
        if len(cost) == 0:
            break
        second = heapq.heappop(cost)
        result += first + second
        heapq.heappush(cost, first + second)
    print(result)
