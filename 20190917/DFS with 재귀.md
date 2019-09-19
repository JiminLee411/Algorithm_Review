# DFS with 재귀

**problems.kr**

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

  

#### 4. [1405.미친 로봇](https://www.acmicpc.net/problem/1405)



#### SWEA

* 1210 - ladder1
* 4613 - 러시아 국기 같은 깃발
* 4875 - 미로(stack2)
