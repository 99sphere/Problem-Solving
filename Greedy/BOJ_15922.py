# BOJ 15922
# Author: Gu Lee
# Date: 2021.09.21
# Source: https://www.acmicpc.net/problem/15922

import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
answer = 0

start = lines[0][0]
end = lines[0][1]

for i in range(1,n):
    if lines[i][0] <= end:
        end = max(end, lines[i][1])
        
    else:
        answer += end - start
        start = lines[i][0]
        end = lines[i][1]
        
answer += end - start
print(answer)
