# BOJ 1826
# Author: Gu Lee
# Date: 2022.01.21
# Source: https://www.acmicpc.net/problem/1826

import heapq

n = int(input())

gas_stations = []


for i in range(n):
  # a is distance from start positon to gas station, and b is amount of new fuel
  a, b = map(int, input().split())
  heapq.heappush(gas_stations, (a, -b))

L, P = map(int, input().split())
# L is distance from start postion to town, and P is amount of fuel

if L <= P:
  # If we can arrive with the remaining fuel
  print(0)

else:
  result = 0
  gas_heap= []
  current_pos = 0

  while True:
    # 주유소에 더 방문하지 않고도 도착할 수 있는 경우
    if current_pos + P >= L:
      print(result)
      break

    # 주유소에 들러야 하는 경우    
    while gas_stations:
      # 가까운 순으로 주유소 탐색
      info = gas_stations[0]
      if info[0] - current_pos <= P:
        # 갈 수 있는 주유소인 경우 gas_heap에 추가
        distance, gas = heapq.heappop(gas_stations)
        heapq.heappush(gas_heap, (gas, distance))
      else:
        break

    if gas_heap:
      max_gas, dist = heapq.heappop(gas_heap)
      #방문할 수 있는 주유소들 중, 가장 많은 gas를 얻을 수 있는 주유소로 이동
      P -= dist - current_pos
      P -= max_gas
      current_pos = dist
      result += 1
    
    else:
      print(-1)
      break
