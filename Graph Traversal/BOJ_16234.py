# BOJ 16234
# Author: Gu Lee
# Date: 2022.09.06
# Source: https://www.acmicpc.net/problem/16234

from collections import deque

N, L, R = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0
end_flag = False

while True:
    visited = [[False] * N for _ in range(N)]
    queue = deque()
    new_graph = [[0] * N for _ in range(N)]     
    updated = False
    for i in range(N):
        for j in range(N):
            cnt = 0
            peoples = 0
            if visited[i][j] == False:
                queue.append((i, j)) 
                cnt += 1
                peoples += graph[i][j]
                track = [(i, j)]
                while queue:
                    dx = [1, -1, 0, 0]
                    dy = [0, 0, 1, -1]

                    start = queue.popleft()
                    
                    start_y, start_x = start[0], start[1]
                    
                    visited[start_y][start_x] = True

                    for k in range(4):
                        new_x = start_x + dx[k]
                        new_y = start_y + dy[k]
                        
                        if 0 <= new_x < N and 0 <= new_y < N: 
                            if visited[new_y][new_x] == False and (new_y, new_x) not in track:
                                if L <= abs(graph[start_y][start_x] - graph[new_y][new_x]) <= R:
                                    updated = True
                                    queue.append((new_y, new_x))
                                    track.append((new_y, new_x))
                                    cnt += 1
                                    peoples += graph[new_y][new_x]
                
                for (y, x) in track:
                    new_graph[y][x] = (peoples // cnt)
                cnt = 0
                peoples = 0 

    if not updated:
        break

    else:
        answer += 1

    graph = new_graph
    
print(answer)
