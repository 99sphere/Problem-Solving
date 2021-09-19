# BOJ 2437
# Author: Gu Lee
# Date: 2021.09.19
# Source: https://www.acmicpc.net/problem/2437

n = int(input())
weights = list(map(int, input().split()))
weights.sort()
num = 1
for i in range(n):
  if num < weights[i]:
    break
  num += weights[i]
print(num)
