# BOJ 13164
# Author: Gu Lee
# Date: 2021.09.21
# Source: https://www.acmicpc.net/problem/13164

import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
children = list(map(int, input().split())) # n개
diff = [children[i+1]-children[i] for i in range(n-1)] # n-1개
diff.sort()

result = 0
for i in range(n-k):
    result += diff[i]
print(result)
