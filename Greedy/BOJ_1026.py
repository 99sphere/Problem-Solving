# BOJ 1026
# Author: Gu Lee
# Date: 2022.08.17
# Source: https://www.acmicpc.net/problem/1026

import heapq
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

heapq.heapify(B)
A = sorted(A)

answer = 0

while A:
  c = A.pop(-1)
  val = heapq.heappop(B)
  answer += c*val

print(answer)
