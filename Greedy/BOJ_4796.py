# BOJ 4796
# Author: Gu Lee
# Date: 2021.09.19
# Source: https://www.acmicpc.net/problem/4796

num = 1

while True:
  L, P, V = map(int, input().split())
  if L == 0 and P == 0 and V == 0:
    break
  result = L * (V//P) + min(L,V%P)
  print("Case %d: %d" %(num, result))
  num+=1
