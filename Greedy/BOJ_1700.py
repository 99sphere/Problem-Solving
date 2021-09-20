# BOJ 1700
# Author: Gu Lee
# Date: 2021.09.20
# Source: https://www.acmicpc.net/problem/1700

n, k = map(int, input().split())
schd = list(map(int, input().split()))
plugs = []
cnt = 0

for i in range(k):
  # 해당 전자제품이 이미 꽂혀 있는 경우
  if schd[i] in plugs:
    continue

  # 빈 콘센트가 있는 경우
  if len(plugs) < n:
    plugs.append(schd[i])
    continue

  # 플러그를 새로 꽂아야 하는 경우
  next_idx = []

  for j in range(n):
    if plugs[j] in schd[i:]:
      next_idx.append(schd[i:].index(plugs[j]))
    else:
      next_idx.append(101)

  fail_plug_idx = next_idx.index(max(next_idx))
  del plugs[fail_plug_idx]
  plugs.append(schd[i])
  cnt += 1

print(cnt)
