# BOJ 18399
# Author: Gu Lee
# Date: 2021.07.25
# Source: https://www.acmicpc.net/problem/11399

n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
result = 0
for i in range(len(nums)):
  result += sum(nums[:i+1])
print(result)
