# BOJ 1541
# Author: Gu Lee
# Date: 2021.08.13
# Source: https://www.acmicpc.net/problem/1541

eq = input().split("-")

for i in range(len(eq)):
  if "+" in eq[i]:
    tmp = eq[i].split("+")
    for j in range(len(tmp)):
      tmp[j] = int(tmp[j])
    cnt = sum(tmp)
    eq[i] = cnt
result = int(eq[0])
for i in eq[1:]:
  result -= int(i)
print(result)