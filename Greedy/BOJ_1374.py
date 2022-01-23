# BOJ 1374
# Author: Gu Lee
# Date: 2022.01.23
# Source: https://www.acmicpc.net/problem/1374

import heapq

N = int(input())
lectures = []
for i in range(N):
  num, start, end = map(int, input().split())
  heapq.heappush(lectures, [start, end, num])

classroom = []
start, end, num = heapq.heappop(lectures)
heapq.heappush(classroom, end)
while lectures:
  start, end, num = heapq.heappop(lectures)
  if classroom[0] <= start:
    heapq.heappop(classroom)
  heapq.heappush(classroom, end)
print(len(classroom))
