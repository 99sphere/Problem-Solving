# BOJ 11000
# Author: Gu Lee
# Date: 2021.09.20
# Source: https://www.acmicpc.net/problem/11000

import sys
import heapq

input = sys.stdin.readline
n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]
classes = sorted(classes, key= lambda x: x[0])

queue = []
heapq.heappush(queue, classes[0][1])

for i in range(1, n):
  if queue[0] > classes[i][0]:
    heapq.heappush(queue, classes[i][1])
  else:
    heapq.heappop(queue)
    heapq.heappush(queue, classes[i][1])

print(len(queue))
