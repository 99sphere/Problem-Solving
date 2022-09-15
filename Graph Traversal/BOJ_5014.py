# BOJ 5014
# Author: Gu Lee
# Date: 2022.09.15  
# Source: https://www.acmicpc.net/problem/5014

from collections import deque

F, S, G, U, D = map(int, input().split())

queue = deque()
queue.append((S, 0))
visited = [False] * (F+1)
visited[0] = True
nums = [U, -D]

while queue:
    start, cnt = queue.popleft()
    if start == G:
        print(cnt)
        exit()
    visited[start] = True
    for i in range(2):
        next =  start + nums[i]
        if 1 <= next <= F and visited[next] == False:
            queue.append((next, cnt+1))
            visited[next] = True

print("use the stairs")
