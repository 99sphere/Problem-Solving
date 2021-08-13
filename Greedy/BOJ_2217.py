# BOJ 2217
# Author: Gu Lee
# Date: 2021.08.13
# Source: https://www.acmicpc.net/problem/2217

n = int(input())
ropes = []
for i in range(n):
  ropes.append(int(input()))
ropes = sorted(ropes)
cand = []
for i in range(n):
    cand.append(ropes[i]*(n-i))
result = max(cand)
print(result)
