# BOJ 1781
# Author: Gu Lee
# Date: 2021.09.21
# Source: https://www.acmicpc.net/problem/1781

import sys
import heapq

input = sys.stdin.readline

n = int(input())
problems = [list(map(int, input().split())) for _ in range(n)]
problems = sorted(problems)
print(problems)
heap = []
for problem in problems:
    heapq.heappush(heap, problem[1])
    if(problem[0] < len(heap)):
        heapq.heappop(heap)
print(sum(heap))
