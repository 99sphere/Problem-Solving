# BOJ 1927
# Author: Gu Lee
# Date: 2022.08.06
# Source: https://www.acmicpc.net/problem/1927

import heapq
import sys

input=sys.stdin.readline
a = []
array = heapq.heapify(a)

n = int(input())
for i in range(n):
    num = int(input())
    if num == 0 and len(a) == 0:
        print(0)
    elif num == 0:
        print(heapq.heappop(a))
    else:
        heapq.heappush(a, num)
