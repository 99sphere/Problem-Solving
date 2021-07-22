# BOJ 2839
# Author: Gu Lee
# Date: 2021.07.23
# Source: https://www.acmicpc.net/problem/2839

n = int(input())

a = n//5
b = n%5
c = 0

while a>=0:
    if b%3 == 0:
        c = b//3
        break
    a -= 1
    b += 5
        
if b%3 == 0:
    print(a+c)
else:
    print(-1)