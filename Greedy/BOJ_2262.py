# BOJ 2262
# Author: Gu Lee
# Date: 2022.01.22
# Source: https://www.acmicpc.net/problem/2262

import math 
n = int(input())
ranks = list(map(int, input().split()))
ans = 0

def abs_diff(num1, num2):
  return abs(num1-num2)

while len(ranks) > 1:
  pos = ranks.index(max(ranks))
  if pos == 0:
    ans += abs_diff(ranks[pos], ranks[pos+1])
  elif pos == len(ranks)-1:
    ans += abs_diff(ranks[pos], ranks[pos-1])
  else:
    if abs_diff(ranks[pos], ranks[pos-1]) > abs_diff(ranks[pos], ranks[pos+1]):
      ans += abs_diff(ranks[pos], ranks[pos+1])
    else:
      ans += abs_diff(ranks[pos], ranks[pos-1])
  ranks.pop(pos)
print(ans)
