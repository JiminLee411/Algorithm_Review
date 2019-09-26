# Algorithm 보충

## DFS with 재귀 (20190917)

**[problems.kr](problems.kr)**

### BOJ

#### 1. [2606.바이러스](https://www.acmicpc.net/problem/2606)

* 글로벌 변수 이용

  ```PYTHON
  CNT = 0
  
  def DFS(v):
      global CNT
      visit[v] = 1
      for w in G[v]:
          if not visit[w]:
              visit[w] = 1
              CNT += 1
              DFS(w)
      return CNT
  
  pcNum = int(input())
  netNum = int(input())
  
  G = [[] for _ in range(pcNum + 1)]
  visit = [0 for _ in range(pcNum + 1)]
  
  for _ in range(netNum):
      u, V = map(int, input().split())
      G[u].append(V)
      G[V].append(u)
  
  res = DFS(1)
  print(res)
  ```

* 로컬 변수 이용

  ```PYTHON
  def DFS(v):
      visit[v] = 1
      cnt = 1
      for w in G[v]:
          if not visit[w]:
              cnt += DFS(w)
      return cnt
  
  pcNum = int(input())
  netNum = int(input())
  
  G = [[] for _ in range(pcNum + 1)]
  visit = [0 for _ in range(pcNum + 1)]
  
  for _ in range(netNum):
      u, V = map(int, input().split())
      G[u].append(V)
      G[V].append(u)
  
  res = DFS(1) - 1
  print(res)
  ```

  

#### 2. [2667.단지번호붙이기](https://www.acmicpc.net/problem/2667)

* 런타임 에러

  ```python
  CNT = 0
  N = int(input())
  
  def DFS(r, c, id):
      global CNT
      global N
      visit[r][c] = 1
      map[r][c] = id
      for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
          if 0<=r+y<N and 0<=c+x<N and map[r + y][c + x] != 0 and visit[r+y][c+x] == 0:
              CNT += 1
              DFS(r + y, c + x, id)
  
  map = [list(map(int, input())) for _ in range(N)]
  visit = [[0]*7 for _ in range(N)]
  t = []
  id = 0
  for r in range(N):
      for c in range(N):
          if map[r][c] != 0 and visit[r][c] == 0:
              id += 1
              DFS(r, c, id)
              t.append(CNT + 1)
              CNT = 0
  t.sort()
  print(len(t))
  
  for res in t:
      print(res)
  ```

* **PASS** : visit배열을 지우고 cnt를 local 변수로 변경

  ```python
  N = int(input())
  
  def DFS(r, c, cnt):
      global N
      map[r][c] = 0
      for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
          if 0<=r+y<N and 0<=c+x<N and map[r + y][c + x] == 1:
              cnt = DFS(r + y, c + x, cnt + 1)
      return cnt
  
  map = [list(map(int, input())) for _ in range(N)]
  res = []
  
  for r in range(N):
      for c in range(N):
          if map[r][c] == 1:
              res.append(DFS(r, c, 1))
  
  print(len(res))
  for i in sorted(res):
      print(i)
  ```

  

#### 3. [10026.적록색약](https://www.acmicpc.net/problem/10026)

* **틀렸습니다** : 테스트케이스 답은 나온다

  ```python
  cnt = [0, 0]
  
  def Find(i):
      for r in range(N):
          for c in range(N):
              if visit[r][c] == 0:
                  DFS(r, c)
                  cnt[i] += 1
  def DFS(r,c):
      global stage
      visit[r][c] = 1
      for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
          if 0 <= r + y < N and 0 <= c + x < N and visit[r + y][c + x] == 0:
              if stage[r][c] == stage[r + y][c + x]:
                  DFS(r + y, c + x)
              elif (stage[r][c] == 'R' and stage[r + y][c + x] == 'G') or (stage[r][c] == 'G' and stage[r + y][c + x] == 'R'):
                  stage[r + y] = stage[r + y][:c + x] + stage[r][c] + stage[r + y][c + x + 1:]
  
  N = int(input())
  stage = [input() for _ in range(N)]
  visit = [[0]*N for _ in range(N)]
  Find(0)
  visit = [[0]*N for _ in range(N)]
  Find(1)
  print('{} {}'. format(cnt[0], cnt[1]))
  ```

  * **문자를 바꾸면 다시 센다!**
  
* **PASS** : 적록색약일때 따로 계산할 수 있게 구현

  ```python
  import sys
  
  sys.setrecursionlimit(10**6)
  
  cnt = [0, 0]
  
  def Find(i):
      for r in range(N):
          for c in range(N):
              if visit[r][c] == 0:
                  DFS(r, c, i)
                  cnt[i] += 1
                  
                  
  def DFS(r,c , i):
      global stage
      visit[r][c] = 1
      for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
          if 0 <= r + y < N and 0 <= c + x < N and visit[r + y][c + x] == 0 and i == 0:
              if stage[r][c] == stage[r + y][c + x]:
                  DFS(r + y, c + x, i)
              elif (stage[r][c] == 'R' and stage[r + y][c + x] == 'G') or (stage[r][c] == 'G' and stage[r + y][c + x] == 'R') and i == 1:
                  DFS(r + y, c + x, i)
  
                  
  N = int(input())
  stage = [input() for _ in range(N)]
  visit = [[0]*N for _ in range(N)]
  Find(0)
  visit = [[0]*N for _ in range(N)]
  Find(1)
  
  print('{} {}'. format(cnt[0], cnt[1]))
  ```

  

#### 4. [~~1405.미친 로봇~~](https://www.acmicpc.net/problem/1405) 





### SWEA

#### 1.[1210_Ladder1](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE)

* **PASS**

  ```python
  def DFS(x, y):
      if x == 0:
          return y
      arr[x][y] = 0
      if y - 1 >= 0 and arr[x][y - 1]:
          return DFS(x, y - 1)
      elif y + 1 < 100 and arr[x][y + 1]:
          return DFS(x, y + 1)
      else:
          return DFS(x - 1, y)
   
  for _ in range(10):
      tc = int(input())
      arr = [list(map(int, input().split())) for _ in range(100)]
   
      x = y = 0
      for i in range(100):
          if arr[99][i] == 2:
              x, y = 99, i
              break
   
      print('#{} {}'. format(tc, DFS(x, y)))
  ```

* 코드 간소화

  ```python
  def DFS(r, c):
      ladder[r][c] = 0
  
      if r == 0:
          return c
      if c - 1 >= 0 and ladder[r][c - 1]:
          return DFS(r, c - 1)
      elif c + 1 < 100 and ladder[r][c + 1]:
          return DFS(r, c + 1)
      else:
          return DFS(r - 1, c)
  
  for _ in range(10):
      tc = int(input())
      ladder = [list(map(int, input().split())) for _ in range(100)]
  
      c = ladder[99].index(2)
  
      print('#{} {}'. format(tc, DFS(99, c)))
  ```

  

#### 2. [4613_러시아 국기 같은 깃발](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj&categoryId=AWQl9TIK8qoDFAXj&categoryType=CODE)

* **PASS** : 반복으로 품.

  ```python
  def Find():
      cnt = 0xffffff
  
      for w in range(N - 2):
          for r in range(w + 2, N):
              tmp = 0
              for i in range(N):
                  if i <= w:
                      tmp += origin[i].count('R')
                      tmp += origin[i].count('B')
                  elif i >= r:
                      tmp += origin[i].count('W')
                      tmp += origin[i].count('B')
                  else:
                      tmp += origin[i].count('R')
                      tmp += origin[i].count('W')
  
              cnt = min(cnt,tmp)
  
      return cnt
  
  
  for tc in range(1, int(input()) + 1):
      N, M = map(int, input().split())
      origin = [input() for _ in range(N)]
  
      res = Find()
  
      print('#{} {}'. format(tc, res))
  ```

  

#### 3. [4875_미로](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do#none)

* **PASS**

  ```python
  def DFS(r, c, n):
      dx = [-1, 0, 1, 0]
      dy = [0, -1, 0, 1]
      visit[r][c] = True
      for i in range(4):
          if (r == N - 1 and i == 3) or (r == 0 and i == 1) or (c == N - 1 and i == 2) or (c == 0 and i == 0):
              continue
          elif maze[r + dy[i]][c + dx[i]] == '3':
              return 1
          elif (visit[r + dy[i]][c + dx[i]] == False) and maze[r + dy[i]][c + dx[i]] == '0':
              if DFS(r + dy[i], c + dx[i], n) == 1:
                  return 1
      return 0
  
  for t in range(1, int(input()) + 1):
      res = 0
      N = int(input())
      maze = [input() for _ in range(N)]
      visit = [[False] * N for _ in range(N)]
      for i in range(N):
          if '2' in maze[i]:
              column = maze[i].find('2')
              row = i
              break
      res = DFS(row, column, N)
      print('#{} {}'. format(t, res))
  ```
  
  

## 조합 생성 (20190919)

### 순열/조합

* 순열/조합 생성 : 백트래킹 이해

* 순열/조합 생성하는 방법(과정) : 재귀호출로

  * 상태 공간 트리 : 재귀 함수 호출 트리

  * 선택의 과정

    ```python
    # 재귀함수호출트리
    # 부분 집합을 생성
    # 원소의 수 = N
    # N번의 선택을 통해서 부분집합 생성, 각각의 원소에 대해서
    # 매번 선택할 때의 선택지 : 2
    path = [0] * 3
    def subset(k, n):
        if k == n:
            print(path)
            return
        # 함수호출이 선택이다.
        path[k] = -1; subset(k + 1, n)
        path[k] = 1; subset(k + 1, n)
        
    subset(0,3)
    ```



  * 순열 생성 - 모든 순열을 생성하는 과정을 선택의 과정
  
    ```python
    N = 3
    # 중복순열
    for i in range(N):
        for j in range(N):
            for k in range(N):
    			print(i, j, k)
                
    # 순열
    visit = [0] * 3
    for i in range(N):
        visit[i] = 1
        for j in range(N):
            if visit[j]: continue
                visit[j] = 1
            for k in range(N):
    			if visit[k]: continue
                visit[k] = 1     
                print(i, j, k)
                visit[k] = 0
            visit[j] = 0
         visit[i] = 0
    # 같은패턴 반복
    visit = [0] * 3
    for i in range(N):
        if visit[i]: continue
        visit[i] = 1
        #-----------------------------
        for j in range(N):
            if visit[j]: continue
                visit[j] = 1
            #--------------------------
            for k in range(N):
    			if visit[k]: continue
                visit[k] = 1     
                print(i, j, k)
                visit[k] = 0
            #-----------------------------
            visit[j] = 0
         #-------------------------
         visit[i] = 0
    # 재귀호출 ( 같은패턴 지우기)
    visit = [0] * 3
    def perm(k, n):
        if k == n:
            return
        
    	for i in range(N):
        	if visit[i]: continue
        	visit[i] = 1
     		perm(k + 1, n)
         	visit[i] = 0
            
    perm(0, N)
    ```
  
  * 조합 생성 (`5C3`)
  
    ```python
    arr = 'ABCDE'
    N = 5
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
    	        print(arr[i], arr[j], arr[k])
                
    arr = 'ABCDE'
    N, R = 5, 3
    def comb(k, s): # s : 선택할 요소의 시작값
        if k ==R:
            print(choose)
            return
        
        for i in range(s, N):
            choose.append(arr[i])
            comb(k + 1, i + 1)
            choose.pop()
        
    comb(0, 0)
    ```




### BOJ

#### 1. [N과 M](https://www.acmicpc.net/workbook/view/2052)

##### 1.1 [15649_N과 M(1)](https://www.acmicpc.net/problem/15649)

* **PASS**

  ```python
  N, M = map(int,input().split())
  
  order = []
  used = [0] * N
  
  def perm(k, n, m):
      if k == m:
          print(' '.join(order))
          return
  
      for i in range(n):
          if used[i]: continue
          used[i] = 1
          order.append(str(i+1))
          perm(k + 1, n, m)
          used[i] = 0
          order.pop()
  
  perm(0, N, M)
  ```

##### 1.2 [15650_N과 M(2)](https://www.acmicpc.net/problem/15650)

* **PASS**

  ```python
  def perm(k, n, m):
      if k == m:
          print(' '.join(order))
          return
      for i in range(N):
          if visit[i] or (order and int(order[-1]) >= i + 1): continue
          visit[i] = 1
          order.append(str(i+1))
          perm(k + 1, n, m)
          visit[i] = 0
          order.pop()
  
  
  N, M = map(int, input().split())
  visit = [0] * N
  order = []
  perm(0, N, M)
  ```

##### 1.3  [15651_N과 M(3)](https://www.acmicpc.net/problem/15651)

* **PASS**

  ```python
  def perm(k, n, m):
      if k == m:
          print(' '.join(order))
          return
      for i in range(N):
          # if order and int(order[-1]) > i + 1: continue
          order.append(str(i+1))
          perm(k + 1, n, m)
          order.pop()
  
  N, M = map(int, input().split())
  order = []
  perm(0, N, M)
  ```

##### 1.4  [15652_N과 M(4)](https://www.acmicpc.net/problem/15652)

* **PASS**

  ```python
  def perm(k, n, m):
      if k == m:
          print(' '.join(order))
          return
      for i in range(N):
          if order and int(order[-1]) > i + 1: continue
          order.append(str(i+1))
          perm(k + 1, n, m)
          order.pop()
  
  N, M = map(int, input().split())
  order = []
  perm(0, N, M)
  ```

  

#### 2. [2798_블랙잭](https://www.acmicpc.net/problem/2798)

* **PASS** : 재귀

  ```PYTHON
  RES = 0
  def Find(k, tmp, n, m):
      global RES
      if k == 3:
          if RES < tmp:
              RES = tmp
          return
      for i in range(N):
          if visit[i] == 1 or tmp + cards[i] > m: continue
          visit[i] = 1
          order.append(cards[i])
          tmp += cards[i]
          Find(k + 1, tmp, n, m)
          visit[i] = 0
          order.pop()
          tmp -= cards[i]
  
  N, M = map(int, input().split())
  cards = list(map(int, input().split()))
  visit = [0] * N
  order = []
  tmp = 0
  Find(0, tmp, N, M)
  print(RES)
  ```

* **PASS** : 일반 순열 -> 코드, 시간 단축

  ```python
  N, M = map(int, input().split())
  cards = list(map(int, input().split()))
  
  res = 0
  for first in range(N):
      for second in range(first + 1, N):
          for third in range(second + 1, N):
              tmp = cards[first] + cards[second] + cards[third]
              if res < tmp <= M:
                  res = tmp
  print(res)
  ```

  

#### 3. [2309_일곱난쟁이](https://www.acmicpc.net/problem/2309)

* **틀렸습니다**

  ```python
  res = 0
  def perm(i, num):
      global res
      visit[i] = 1
  
      if num == 7:
          for i in sorted(cnt):
              print(i)
          return 1
  
      for j in range(9):
          if res == 1: break
          if visit[j] or sum(cnt) + smallMen[j] > 100:
              continue
          cnt.append(smallMen[i])
          res = perm(j, num + 1)
          if res == 1: break
          cnt.pop()
          visit[j] = 0
  
  smallMen = [ int(input()) for _ in range(9)]
  visit = [0 for _ in range(9)]
  cnt = []
  perm(0, 0)
  ```

  

#### 4. [6603_로또](https://www.acmicpc.net/problem/6603)



#### 5. [3980_선발명단](https://www.acmicpc.net/problem/3980)



### SWEP

#### 1. [2817_부분수열의 합]()

* **FAIL** : 같은 수열의 합이 2번씩 반복.

  ```python
  def sumNum(tmp, used):
      global cnt
      if tmp == K:
          cnt += 1
          return
      for i in range(N):
          if used & 1<<i:
              continue
          res.append(arr[i])
          sumNum(tmp + arr[i], used|1<<i)
          res.pop()
  
  for tc in range(1, int(input()) + 1):
      N, K = map(int, input().split())
      arr = list(map(int, input().split()))
      res = []
      cnt = 0
      sumNum(0, 0)
      print('#{} {}'. format(tc, cnt))
  ```

* **PASS** : for문이 시작하는 부분을 만들어 준다.

  ```python
  def sumNum(k, tmp, used):
      global cnt
      if tmp == K:
          cnt += 1
          return
      for i in range(k, N):
          if used & 1<<i:
              continue
          res.append(arr[i])
          sumNum(i+1, tmp + arr[i], used|1<<i)
          res.pop()
  
  for tc in range(1, int(input()) + 1):
      N, K = map(int, input().split())
      arr = list(map(int, input().split()))
      res = []
      cnt = 0
      sumNum(0, 0, 0)
      print('#{} {}'. format(tc, cnt))
  ```

  

#### 2. [2806_N-Queen]()





