# BOJ 13904
# Author: Gu Lee
# Date: 2021.09.21
# Source: https://www.acmicpc.net/problem/13904

import sys

input = sys.stdin.readline
n = int(input())

assignments = [list(map(int, input().split())) for _ in range(n)]
assignments = sorted(assignments, key = lambda x: (-x[1], x[0]))

schd = [0] * 1001

for assignment in assignments:
    idx = assignment[0]
    score = assignment[1]
    for i in range(idx, 0, -1):
        if score > schd[i]:
            schd[i] = score
            break
        
print(sum(schd))
