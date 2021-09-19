# BOJ 1715
# Author: Gu Lee
# Date: 2021.09.19
# Source: https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
cards = list(int(input()) for _ in range(n))
heapq.heapify(cards)
result = 0

while len(cards) != 1:
  num1 = heapq.heappop(cards)
  num2 = heapq.heappop(cards)
  sum = num1+num2
  result += sum
  heapq.heappush(cards, sum)

print(result)
