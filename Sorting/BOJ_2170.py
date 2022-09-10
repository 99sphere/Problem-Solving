# BOJ 2170
# Author: Gu Lee
# Date: 2022.09.10
# Source: https://www.acmicpc.net/problem/2170

import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

lines.sort()

p_start, p_end = lines[0][0], lines[0][1]

ans = 0

for i in range(1, n):
    start, end = lines[i][0], lines[i][1]
    if start < p_end:
        p_end = max(p_end, end)
    else:
        ans += p_end - p_start
        p_start, p_end = start, end

ans += p_end - p_start

print(ans)
