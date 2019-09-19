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