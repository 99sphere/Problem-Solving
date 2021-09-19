# BOJ 1202
# Author: Gu Lee
# Date: 2021.09.19
# Source: https://www.acmicpc.net/problem/1202

import heapq
import sys

n, k = map(int, sys.stdin.readline().split())
jewels = []
for _ in range(n):
  heapq.heappush(jewels, list(map(int, sys.stdin.readline().split())))
bags = [int(sys.stdin.readline()) for _ in range(k)]
bags.sort()

result = 0
cand_jew = []
for bag in bags:
  while jewels and bag >= jewels[0][0]:
    heapq.heappush(cand_jew, -heapq.heappop(jewels)[1])
  if cand_jew:
    result -= heapq.heappop(cand_jew)
  elif not jewels:
    break

print(result)
