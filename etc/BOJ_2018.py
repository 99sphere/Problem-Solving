# BOJ 2018
# Author: Gu Lee
# Date: 2022.10.22
# Source: https://www.acmicpc.net/problem/2018

n = int(input())
ans, temp = 0, 0
start, end = 0, 0

while end <= n:
    if temp < n:
        end += 1
        temp += end
    
    elif temp > n:
        temp -= start
        start += 1
        
    else:
        ans += 1
        end += 1
        temp += end

print(ans)
