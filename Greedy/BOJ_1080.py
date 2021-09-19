# BOJ 1080
# Author: Gu Lee
# Date: 2021.09.19
# Source: https://www.acmicpc.net/problem/1080

n, m = map(int, input().split())
mat_A = [list(map(int, input())) for _ in range(n)]
mat_B = [list(map(int, input())) for _ in range(n)]
result = 0

def convert_3x3(x, y):
  for i in range(x, x+3):
    for j in range(y, y+3):
      mat_A[i][j] = 1 - mat_A[i][j]
 
for i in range(n-2):
  for j in range(m-2):
    if mat_A[i][j] != mat_B[i][j]:
      convert_3x3(i, j)
      result += 1
  
if mat_A == mat_B:
  print(result)
else:
  print(-1)
