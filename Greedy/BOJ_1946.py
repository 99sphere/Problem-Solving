# BOJ 1946
# Author: Gu Lee
# Date: 2021.07.15
# Source: https://www.acmicpc.net/problem/1946

import sys

t = int(input())

for i in range(0, t):
  result = 1  
  n = int(input())
  cand = []
  
  for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    cand.append(temp)
      
  cand.sort() 
  
  max = cand[0][1]  
  for i in range(1,n):
    if max > cand[i][1]:
      result += 1
      max = cand[i][1]

  print(result)