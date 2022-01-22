# BOJ 1092
# Author: Gu Lee
# Date: 2022.01.22
# Source: https://www.acmicpc.net/problem/1092

import heapq

N = int(input())
limits = sorted(list(map(int,input().split())), reverse=True)
M = int(input())
weights = sorted(list(map(int,input().split())), reverse=True)

ans = 0

if max(weights) > max(limits):
  print(-1)

else:
  while len(weights):
    ans += 1
    for i in range(len(limits)):
      for j in range(len(weights)):
        if limits[i] >= weights[j]:
          weights.pop(j)
          break

  print(ans)
"""
반례
2
1 10
8
1 1 1 1 10 10 10 10
6
"""
