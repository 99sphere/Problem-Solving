# BOJ 9576
# Author: Gu Lee
# Date: 2021.09.20
# Source: https://www.acmicpc.net/problem/9576

import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
  n, m = map(int, input().split())
  ranges = [list(map(int, input().split())) for _ in range(m)]
  books = [False for _ in range(n+1)]

  ranges = sorted(ranges, key=lambda x: (x[1], x[0]))

  result = 0

  for j in ranges:
    for k in range(j[0], j[1]+1):
      if books[k] == False:
        books[k] = True
        result += 1
        break

  print(result)
