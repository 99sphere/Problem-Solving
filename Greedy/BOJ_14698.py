# BOJ 14698
# Author: Gu Lee
# Date: 2021.09.22
# Source: https://www.acmicpc.net/problem/14698

import sys
input = sys.stdin.readline
import heapq

T = int(input())
for i in range(T):
    n = int(input())
    if n == 1:
        input()
        print(1)
        continue
    else:
        slimes = list(map(int, input().split()))
        heapq.heapify(slimes)
        result = 1
        while True:
            first = heapq.heappop(slimes)
            if len(slimes) == 0:
                print(result%1000000007)
                break
            second = heapq.heappop(slimes)
            result *= (first * second)
            heapq.heappush(slimes, first*second)
        
