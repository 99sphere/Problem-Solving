# Algorithm Study

*****

## 1. Greedy Algorithm
> **현재 상황에서 가장 좋아보이는 것만을 선택하는 알고리즘**

- 탐욕법. 현재 상황에서 가장 최선의 것만 고르는 방식. 보통 문제에서 제시하는 기준에 따라, 각 상황에서 **가장 최선의 (보통 가장 큰 순서대로 or 가장 작은 순서대로) 선택**을 하면 된다. 
- 이로 인해 자주 정렬 알고리즘과 짝을 이뤄 출제되는데, 문제 해결에는 보통 heapsort를 이용하더라. heapq 라이브러리를 이용하면 O(log n) 으로 정렬이 가능하다.

### :rocket: Greedy Algorithm Example :rocket:
- [BOJ_14698](https://www.acmicpc.net/problem/14698), [Solution](https://github.com/99sphere/Problem-Solving/blob/main/Greedy/BOJ_14698.py)      

*****

## 2. Implementation    
> **머릿속에 있는 알고리즘을 정확하고 빠르게 프로그램으로 작성하기**

- 구현이란, '머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정'이다. 흔히 문제 해결 분야에서의 구현 유형은 '풀이를 떠올리는 것은 쉽지만, 소스코드로 옮기기 어려운 문제'를 의미한다. 
- 완전탐색과 시뮬레이션 유형을 묶어서 구현 유형으로 다루는데, 완전탐색은 모든 경우의 수를 주저없이 다 계산하는 해결방법을 의미하고, 시뮬레이션은 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제유형을 의미한다.   
- 구현 시 , 메모리 제약 사항을 고려해야 한다. 보통 코딩테스트에서는 128 ~ 512MB로 메모리를 제한한다. 파이썬에서 리스트의 크기는 아래와 같다.     


데이터의 개수(리스트의 길이)|메모리 사용량|
:---:|:---:|
1,000|약 4KB|
1,000,000|약 4MB|
10,000,000|약 40MB|

### :rocket: Implementation Example :rocket:      

*****

## 3. Graph Traversal (DFS/BFS)
> **그래프를 탐색하기 위한 대표적인 두 가지 알고리즘**
- 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 의미한다. 프로그래밍에서는 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 주로 다룬다. 대표적인 탐색 알고리즘으로 **DFS**와 **BFS**를 꼽을 수 있는데, 이 두 알고리즘의 원리를 제대로 이해해야 코딩테스트의 탐색 문제 유형을 풀 수 있다. 그런데 DFS와 BFS를 제대로 이해하려면 기본 자료구조인 스택과 큐에 대한 이해가 전제되어야 하므로, 이에 대해 간단히 정리해보자.

### 스택
- **스택**은 박스 쌓기에 비유할 수 있다. 흔히 박스는 아래에서부터 위로 차곡차곡 쌓는다. 그리고 아래에 있는 박스를 치우기 위해서는 위에 있는 박스를 먼저 내려야 한다. 이러한 구조를 FILO(First In Last Out) 구조 또는 LIFO(Last In First Out) 구조라고 한다. 
- 파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작한다. append() 메서드는 리스트의 가장 뒤쪽에 데이터를 삽입하고, pop() 메서드는 리스트의 가장 뒤쪽에서 데이터를 꺼내기 때문이다.

### 큐
- **큐**는 대기줄에 비유할 수 있다. 우리가 흔히 놀이공원에 입장하기 위해 줄을 설 때, 먼저 온 사람이 먼저 들어가게 된다. 물론  새치기는 없다고 가정한다. 나중에 온 사람일수록 나중에 들어가기 때문에 흔히 '공정한' 자료구조라고 비유된다. 이러한 구조를 FIFO(First In First Out) 구조라고 한다.
- 파이썬에서 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용하자. deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다.

### 재귀함수
- DFS와 BFS를 구현하려면 재귀함수도 이해하고 있어야 한다.
*****
## 4. Sorting
*****
## 5. Binary Search

*****
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
        
##### 2021.01.21
    Greedy - BOJ_1826

##### 2021.01.22
    Greedy - BOJ_1092
    Greedy - BOJ_2262
        
##### 2021.01.22
    Greedy - BOJ_1374
        
##### 2021.01.28
    Greedy - BOJ_5430
        
##### 2021.01.30
    DP - BOJ_11659
        
##### 2021.02.06
    Graph Traversal - BOJ_2178
    Graph Traversal - BOJ_2667
    Graph Traversal - BOJ_1012
        
##### 2021.02.12
    Graph Traversal - BOJ_7576   
    Graph Traversal - BOJ_10026 (Python3 시간초과, PyPy3 통과)   
    Graph Traversal - BOJ_7569
    Graph Traversal - BOJ_1987
</div>
</details>

