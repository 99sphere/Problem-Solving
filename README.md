# Algorithm Study

## 1. Greedy
탐욕법. 이름에서 알 수 있듯이 문제에서 제시하는 기준에 따라, 각 상황에서 가장 적합한(보통 최대 or 최소) 선택을 하면 된다. 이로 인해 sorting을 자주 하게 되는데, 보통 heapsort를 이용하더라.


<details>
<summary><b>Greedy Example</b></summary>
<div markdown="1">
        """
        BOJ 14698
        Author: Gu Lee
        Date: 2021.09.22
        Source: https://www.acmicpc.net/problem/14698
        """
        
        import sys
        input = sys.stdin.readline
        import heapq

        T = int(input())
        for i in range(T):
            n = int(input())
            if n == 1:
                input()
                print(1)
                continue
            else:
                slimes = list(map(int, input().split()))
                heapq.heapify(slimes)
                result = 1
                while True:
                    first = heapq.heappop(slimes)
                    if len(slimes) == 0:
                        print(result%1000000007)
                        break
                    second = heapq.heappop(slimes)
                    result *= (first * second)
                    heapq.heappush(slimes, first*second)
</div>
</details>




<details>
<summary><b>History</b></summary>
<div markdown="1">

##### 2021.07.06
    Implementation - BOJ_2941   
  
##### 2021.07.23
    Greedy - BOJ_2839   
  
##### 2021.07.25
    Greedy - BOJ_11399   
  
##### 2021.07.28
    Greedy - BOJ_11047   
  
##### 2021.07.31
    Greedy - BOJ_1931   
  
##### 2021.08.13
    Greedy - BOJ_1541   
    Greedy - BOJ_5585
    Greedy - BOJ_2217
    
##### 2021.08.14
    Greedy - BOJ_10162   

##### 2021.08.15
    Greedy - BOJ_1946
    
    
##### 2021.09.19
    Greedy - BOJ_1789
    Greedy - BOJ_1715
    Greedy - BOJ_4796
    Greedy - BOJ_1744
    Greedy - BOJ_1080
    Greedy - BOJ_1202
    Greedy - BOJ_2437
    
##### 2021.09.20
    Greedy - BOJ_1700
    Greedy - BOJ_11000
    Greedy - BOJ_9576   

##### 2021.09.21
    Greedy - BOJ_13904
    Greedy - BOJ_12904
    Greedy - BOJ_2109
    Greedy - BOJ_1461
    Greedy - BOJ_1781 --> 왜 맞았지?
    Greedy - BOJ_13164
    Greedy - BOJ_16120
    Greedy - BOJ_15922

##### 2021.09.22
    Greedy - BOJ_2141
    Greedy - BOJ_1339
</div>
</details>

