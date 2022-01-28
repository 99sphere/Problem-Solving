# BOJ 5430
# Author: Gu Lee
# Date: 2022.01.27
# Source: https://www.acmicpc.net/problem/5430

t = int(input())
for i in range(t):
  p = input()
  n = int(input())
  nums = input()[1:-1].split(",")
  r = 0
  error_flag = 0
  
  if n == 0 and "D" in p:
    print("error")
    continue

  for j in range(len(p)):
    if p[j] == "R":
      r += 1
    else:
      if len(nums) == 0:
        error_flag = 1
        print("error")
        break

      else:
        if r % 2 == 1:
          nums.pop()
        else:
          nums.pop(0)

  if error_flag == 0:
    if r%2 == 0:
      print("[" + ",".join(nums) + "]")
    else:
      print("[" + ",".join(reversed(nums)) + "]")
