# BOJ 1049
# Author: Gu Lee
# Date: 2022.08.19
# Source: https://www.acmicpc.net/problem/1049

import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
packages = []
ones = []

for i in range(m):
    pack, one = map(int, input().split())
    heapq.heappush(packages, pack)
    heapq.heappush(ones, one)
answer = 0
while n > 0:
    if n >= 6:
        if packages[0] < ones[0]*6:
            answer += packages[0]
            n -= 6
        else:
            answer += ones[0]*6
            n -= 6
    else:
        if packages[0] < ones[0]*n:
            answer += packages[0]
            n -= n
        else:
            answer += ones[0]*n
            n -= n
print(answer)
