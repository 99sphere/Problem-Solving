# Algorithm Study

*****

## 1. Greedy Algorithm
> **현재 상황에서 가장 좋아보이는 것만을 선택하는 알고리즘**

- 탐욕법. 현재 상황에서 가장 최선의 것만 고르는 방식. 보통 문제에서 제시하는 기준에 따라, 각 상황에서 **가장 최선의 (보통 가장 큰 순서대로 or 가장 작은 순서대로) 선택**을 하면 된다. 
- 이로 인해 자주 정렬 알고리즘과 짝을 이뤄 출제되는데, 문제 해결에는 보통 heapsort를 이용하더라. heapq 라이브러리를 이용하면 O(log n) 으로 정렬이 가능하다.

### :trophy: Greedy Algorithm Example :trophy:
- [BOJ_13975: 파일합치기 3](https://www.acmicpc.net/problem/13975), [~~Solution~~](https://github.com/99sphere/Problem-Solving/blob/main/Greedy/BOJ_13975.py)      

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

### :trophy: Implementation Example :trophy:    

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
- DFS와 BFS를 구현하려면 재귀함수도 이해하고 있어야 한다. 재귀함수란 자기자신을 다시 호출하는 함수를 의미한다. 재귀함수를 이용할때는 **종료 조건**을 꼭 명시해야 한다.
- 컴퓨터 내부에서 재귀함수의 수행은 스택 자료구조를 이용한다. 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문이다. 따라서 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀함수를 이용하여 간단하게 구현할 수 있다. DFS가 대표적인 예이다.

### 그래프
- 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말한다. 이때 그래프는 크게 2가지 방식으로 표현할 수 있다.
- 인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결관계를 표현하는 방식   
<img src="https://user-images.githubusercontent.com/59161083/153702041-336984b6-9357-48d8-844f-e5d0030f227b.png" width="45%" height="50%" alt="인접행렬"></img>

- 인접 리스트(Adjacency List) : 리스트로 그래프의 연결관계를 표현하는 방식     
   <img src="https://user-images.githubusercontent.com/59161083/153702147-43fe53fe-e63f-4f72-ba37-6bae46a31a51.png" width="45%" height="50%" alt="인접리스트"></img>

- 위의 두 방식을 비교해보자. Adjacency Matrix 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비된다. 반면, Adjacency List 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용한다. 하지만 이로 인해 Adjacency List 방식은 Adjacency Matrix 방식에 비해 특정 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다. Adjacency List 방식에서는 연결된 데이터를 하나씩 확인해야 하기 때문이다.

### DFS
- DFS(Depth First Search)는 **깊이 우선 탐색** 이라고도 불리며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다. 동작 과정은 아래와 같다.
> 1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다.
> 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접노드를 스택에 넣고 방문처리를 한다. 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다.
> 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

#### DFS 예제     
<img src="https://user-images.githubusercontent.com/59161083/153702677-43bdc09a-dd1c-4ac4-b040-c4527e7c0f5e.PNG" width="45%" height="50%" alt="인접행렬"></img>
- 노드 1에서 시작한 경우, 노드의 탐색 순서는 (1 → 2 → 7 → 6 → 8 → 3 → 4 → 5) 이다. 
#### DFS 소스코드
```python3
# DFS 메서드 정의
def dfs(graph, v, visited):
   # 현재 노드를 방문처리
   visited[v] = True
   print(v, end='')
   # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
   for i in graph[v]:
      if not visited[i]:
         dfs(graph, i, visited)
 
# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

- 이처럼 DFS는 스택 자료구조에 기초한다는 점에서 구현이 간단하다. 실제로는 스택을 사용하지 않아도 되며, 탐색을 수행함에 있어서 데이터의 개수가 N개인 경우 O(N)의 시간이 소요된다는 특징이 있다.

### BFS
- BFS(Breadth First Search) 알고리즘은 **'너비 우선 탐색'** 이라는 의미를 갖는다. 쉽게 말해 가까운 노드부터 탐색하는 알고리즘이다. DFS는 최대한 멀리 있는 노드를 우선적으로 탐색하는 반면, BFS는 그 반대이다. BFS 구현에는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석이다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행하게 된다.
- BFS의 정확한 동작 방식은 아래와 같다. 
> 1. 탐색시작 노드를 큐에 삽입하고 방문처리를 한다.
> 2. 큐에서 노드를 꺼내 해당 노드의 인접노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다. 
> 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

#### BFS 예제     
<img src="https://user-images.githubusercontent.com/59161083/153702677-43bdc09a-dd1c-4ac4-b040-c4527e7c0f5e.PNG" width="45%" height="50%" alt="인접행렬"></img>
- 노드 1에서 시작한 경우, 노드의 탐색 순서는 (1 → 2 → 3 → 8 → 7 → 4 → 5 → 6) 이다. 
#### BFS 소스코드
```python3
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
   # 큐(Queue) 구현을 위해 deque 라이브러리 사용
   queue = deque([start])
   # 현재 노드를 방문처리
   visited[start] = True
   # 큐가 빌 때까지 반복
   while queue:
      # 큐에서 하나의 원소를 뽑아 출력
      v = queu.popleft()
      print(v, end='')
      # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      for i in graph[v]:
         if not visited[i]:
            queue.append(i)
            visited[i] = True
            
# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 bfs 함수 호출
bfs(graph, 1, visited)
```

- 이처럼 BFS는 큐 자료구조에 기초한다는 점에서 구현이 간단하다. 실제로 구현함에 있어 앞서 언급한대로 deque 라이브러리를 사용하는 것이 좋으며 탐색을 수행함에 있어 O(N)의 시간이 소요된다. 일반적인 경우 **실제 수행시간은 DFS보다 좋은 편**이라는 점까지만 추가로 기억하자.

### :trophy: Graph Traversal Example (DFS/BFS) :trophy:       
- [BOJ_7576: 토마토](https://www.acmicpc.net/problem/7576), [~~Solution~~](https://github.com/99sphere/Problem-Solving/blob/main/Graph%20Traversal/BOJ_7576.py)
- [BOJ_7569: 토마토(윗 문제의 3차원 버전)](https://www.acmicpc.net/problem/7569), [~~Solution~~](https://github.com/99sphere/Problem-Solving/blob/main/Graph%20Traversal/BOJ_7569.py)
*****
## 4. Sorting
> **연속된 데이터를 기준에 따라서 정렬하기 위한 알고리즘**
### 정렬 알고리즘 개요
정렬(sorting)이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다. 데이터를 가공할때 오름차순이나 내림차순으로 정렬해서 사용하는 경우가 많기에 정렬 알고리즘은 프로그램을 작성할때 가장 많이 사용되는 알고리즘 중 하나이다. 정렬 알고리즘으로 데이터를 정렬하면 이진탐색(Binary Search)이 가능해진다. 다양한 정렬 알고리즘들이 존재하지만, 여기서는 선택정렬(Selection Sort), 삽입정렬(Insertion Sort), 퀵정렬(Quick Sort), 계수정렬(Counting Sort)에 대해 다룬다.

### 선택정렬 (Selection Sort)
컴퓨터가 데이터를 정렬할 때 어떻게 할 지 한번 생각해보자. **데이터가 무작위로 여러개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복하면 어떨까?** 이 방법은 가장 원시적인 방법으로 매번 '가장 작은 것을 선택'한다는 의미에서 선택정렬(Selection Sort) 알고리즘이라고 한다. 가장 작은 것을 선택해서 앞으로 보내는 과정을 수행하다보면, 전체 데이터의 정렬이 이루어진다.

#### 선택정렬 소스코드
```python3
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
   min_index = i # 가장 작은 원소의 인덱스
   for j in range(i+1, len(array)):
      if array[min_index] > array[j]:
         min_index = j
   array[i], array[min_index] = array[min_index], array[i]
   
print(array)
```
#### 선택정렬의 시간 복잡도
선택정렬은 N-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다. 또한, 매번 가장 작은 수를 찾기 위한 비교연산이 필요하다. 구현방식에 따라 사소한 오차는 있을 수 있지만, 연산 횟수는 
N + (N-1) + ... + 2로 볼 수 있다. 따라서 Big-Oh 표기법을 이용하여 O(N^2) 이라고 표현할 수 있다.

### 삽입정렬 (Insertion Sort)
선택정렬은 알고리즘 문제풀이에 사용하기에는 느린 편이다. 그렇다면 다른 접근 방법에 대해서 생각해보자. **데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하면 어떨까?** 삽입정렬은 선택정렬처럼 동작원리를 직관적으로 이해하기 쉬운 알고리즘이다. 물론 삽입정렬은 선택정렬에 비해 구현 난이도가 높은 편이지만, 선택정렬에 비해 실행시간 측면에서 훨씬 효율적인 알고리즘으로 잘 알려져 있다. 특히 삽입정렬은 **필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 훨씬 효율적이다.** 선택정렬은 현재 데이터의 상태와 상관없이 무조건 모든 원소를 비교하고 위치를 바꾸는 반면 삽입정렬은 그렇지 않다. 삽입정렬은 특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 삽입정렬(Insertion Sort)이라고 부른다. 더불어 삽입정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다. 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에, 그 위치에 삽인된다는 점이 특징이다.

#### 삽입정렬 소스코드
```python3   
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
   for j in range(i, 0, -1): # i부터 1까지 감소하며 반복
      if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
         array[j], array[j-1] = array[j-1], array[j]
      else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
         break
         
print(array)
```

#### 삽입정렬의 시간복잡도
삽입정렬의 시간복잡도는 O(N^2)인데, 실제로 수행시간을 테스트해보면 선택정렬과 흡사한 시간이 소요되는 것을 알 수 있다. 여기서 꼭 기억할 내용은 삽입정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다는 점이다. 최선의 경우 O(N)의 시간복잡도를 가진다. 이 경우 퀵 정렬 알고리즘보다 더 강력하다.

### 퀵 정렬 (Quick Sort)

*****

## 5. Binary Search

*****

## 6. Dynamic Programming

*****

## 7. Shortest Path
<details>
<summary><b>History</b></summary>
<div markdown="1">

##### 2021.07.06
    > Implementation - BOJ_2941   
  
##### 2021.07.23
    > Greedy - BOJ_2839   
  
##### 2021.07.25
    > Greedy - BOJ_11399   
  
##### 2021.07.28
    > Greedy - BOJ_11047   
  
##### 2021.07.31
    > Greedy - BOJ_1931   
  
##### 2021.08.13
    > > Greedy - BOJ_1541   
    > Greedy - BOJ_5585
    > Greedy - BOJ_2217
    
##### 2021.08.14
    > Greedy - BOJ_10162   

##### 2021.08.15
    > Greedy - BOJ_1946
    
    
##### 2021.09.19
    > Greedy - BOJ_1789
    > Greedy - BOJ_1715
    > Greedy - BOJ_4796
    > Greedy - BOJ_1744
    > Greedy - BOJ_1080
    > Greedy - BOJ_1202
    > Greedy - BOJ_2437
    
##### 2021.09.20
    > Greedy - BOJ_1700
    > Greedy - BOJ_11000
    > Greedy - BOJ_9576   

##### 2021.09.21
    > Greedy - BOJ_13904
    > Greedy - BOJ_12904
    > Greedy - BOJ_2109
    > Greedy - BOJ_1461
    > Greedy - BOJ_1781
    > Greedy - BOJ_13164
    > Greedy - BOJ_16120
    > Greedy - BOJ_15922

##### 2021.09.22
    > Greedy - BOJ_2141
    > Greedy - BOJ_1339
        
##### 2021.01.21
    > Greedy - BOJ_1826

##### 2021.01.22
    > Greedy - BOJ_1092
    > Greedy - BOJ_2262
        
##### 2021.01.22
    > Greedy - BOJ_1374
        
##### 2021.01.28
    > Greedy - BOJ_5430
        
##### 2021.01.30
    > DP - BOJ_11659
        
##### 2021.02.06
    > Graph Traversal - BOJ_2178
    > Graph Traversal - BOJ_2667
    > Graph Traversal - BOJ_1012
        
##### 2021.02.12
    > Graph Traversal - BOJ_7576   
    > Graph Traversal - BOJ_10026 (Python3 시간초과, PyPy3 통과)   
    > Graph Traversal - BOJ_7569
    > Graph Traversal - BOJ_1987
   
##### 2021.02.13
    > Graph Traversal - BOJ_2206

##### 2021.02.15
    > Graph Traversal + Dynamic Programming - BOJ_1520
   
</div>
</details>

