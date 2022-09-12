# BOJ 3055
# Author: Gu Lee
# Date: 2022.09.12
# Source: https://www.acmicpc.net/problem/3055

from collections import deque

r, c = map(int, input().split())

graph = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sonic = deque()  # 고슴도치
water = deque()  # 물
count = 0  # 시간(초) 카운트


for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            water.append((j, i))
            visited[i][j] = True

        elif graph[i][j] == 'S':
            sonic.append((j, i))
            visited[i][j] = True

        elif graph[i][j] == 'X':
            visited[i][j] = True


while sonic:
    for _ in range(len(water)):
        w_x, w_y = water.popleft()
        for j in range(4):
            nx = w_x + dx[j]
            ny = w_y + dy[j]
            if 0 <= nx < c and 0 <= ny < r:
                if graph[ny][nx] == '.':
                    water.append((nx, ny))
                    graph[ny][nx] = '*'
                    visited[ny][nx] = True

    count += 1

    for _ in range(len(sonic)):
        s_x, s_y = sonic.popleft()
        for i in range(4):
            nx = s_x + dx[i]
            ny = s_y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if graph[ny][nx] =='.' and visited[ny][nx] == False:
                    sonic.append((nx, ny))
                    visited[ny][nx] = True
                elif graph[ny][nx] == 'D':
                    print(count)
                    exit()

print("KAKTUS")
