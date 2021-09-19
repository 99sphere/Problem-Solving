# BOJ 1744
# Author: Gu Lee
# Date: 2021.09.19
# Source: https://www.acmicpc.net/problem/1744

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)
pos = []
neg = []
result = 0

for i in range(n):
  if nums[i] > 1:
    pos.append(nums[i])
  elif nums[i] == 1:
    result += 1
  else:
    neg.append(nums[i])

if len(pos) % 2 == 1:
  result += pos[-1] 

for i in range(0, len(pos)-1, 2):
  result += pos[i] * pos[i+1]

if len(neg) % 2 == 1:
    result += neg[0]

for j in range(len(neg)-1, 0, -2):
  result += neg[j] * neg[j-1]

print(result)
